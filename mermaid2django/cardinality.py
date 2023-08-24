class CardinalityExpression:
    def __init__(self, piece=""):
        if len(piece) != 6:
            raise TypeError("missmatch")
        self.piece = piece

    def __str__(self):
        return self.piece

    def is_one_or_zero(self, chop):
        return chop == "|" or chop == "o"

    def is_multi2multi(self):
        return (
            self.piece[0] == "}"
            and self.is_one_or_zero(self.piece[1])
            and self.is_one_or_zero(self.piece[4])
            and self.piece[5] == "{"
        )

    def is_one2one(self):
        return (
            self.piece[0] == "|"
            and self.is_one_or_zero(self.piece[1])
            and self.is_one_or_zero(self.piece[4])
            and self.piece[5] == "|"
        )

    def is_one2multi(self):
        return (
            self.piece[0] == "|"
            and self.is_one_or_zero(self.piece[1])
            and self.is_one_or_zero(self.piece[4])
            and self.piece[5] == "{"
        )

    def is_multi2one(self):
        return (
            self.piece[0] == "}"
            and self.is_one_or_zero(self.piece[1])
            and self.is_one_or_zero(self.piece[4])
            and self.piece[5] == "|"
        )


class CardinalityItem:
    def __init__(self, items=[]):
        (
            left,
            expression,
            right,
            colone,
            memo,
        ) = items
        self.items = items
        self.leaf = (
            left,
            right,
        )
        self.type = ""
        self.expression = CardinalityExpression(expression)
        self.description = memo.strip('"')

    def parse(self):
        if self.expression.is_multi2one():
            (
                left,
                right,
            ) = self.leaf
            self.leaf = (
                right,
                left,
            )
            self.type = "one2multi"
        if self.expression.is_one2multi():
            self.type = "one2multi"
        if self.expression.is_one2one():
            self.type = "one2one"
        if self.expression.is_multi2multi():
            self.type = "multi2multi"

    def is_blongs_to_entity_name(self, entity_name):
        (
            left,
            right,
        ) = self.leaf
        return entity_name == left or entity_name == right

    def __str__(self):
        return "{}--{} :=> {}".format(self.leaf[0], self.leaf[1], self.type)


class CardinalitySet:
    ALL_ENTITIES_NAME = set()

    def __init__(self, all=[]):
        self.cardinalities = set(all)
        for items in all:
            for leaf in items.leaf:
                self.ALL_ENTITIES_NAME.add(leaf)

    @staticmethod
    def is_multi2multi(e: CardinalityItem):
        return e.type == "multi2multi"

    @staticmethod
    def is_one2multi(e: CardinalityItem):
        return e.type == "one2multi"

    @staticmethod
    def is_one2one(e: CardinalityItem):
        return e.type == "one2one"

    def get_cardinalities(self):
        return self.cardinalities

    def is_link_table(self, entity_name=""):
        tmp = entity_name.partition("__")
        if tmp[1] == "" and tmp[2] == "":
            return False
        return tmp[0] in self.ALL_ENTITIES_NAME and tmp[2] in self.ALL_ENTITIES_NAME

    def find_by_entity_name(self, entity_name):
        if entity_name not in self.ALL_ENTITIES_NAME:
            raise RuntimeError("unkown entity name")
        found = []
        for citem in self.cardinalities:
            if citem.is_blongs_to_entity_name(entity_name):
                found.append(citem)
        return found

    def get_multi2multi_all(self):
        return list(filter(self.is_multi2multi, list(self.cardinalities)))

    def get_one2multi_all(self):
        return list(filter(self.is_one2multi, list(self.cardinalities)))

    def get_one2one_all(self):
        return list(filter(self.is_one2one, list(self.cardinalities)))

    def get_multi2multi_by_entity_name(self, entity_name):
        cset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_multi2multi, cset))

    def get_one2multi_by_entity_name(self, entity_name):
        cset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_one2multi, cset))

    def get_one2one_by_entity_name(self, entity_name):
        cset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_one2one, cset))
