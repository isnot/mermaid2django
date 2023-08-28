class RelationshipExpression:
    def __init__(self, piece=""):
        if len(piece) != 6:
            raise TypeError("missmatch")
        self.piece = piece

    def __str__(self):
        return self.piece

    def is_one_or_zero(self, piece):
        return piece == "|" or piece == "o"

    def is_many2many(self):
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

    def is_one2many(self):
        return (
            self.piece[0] == "|"
            and self.is_one_or_zero(self.piece[1])
            and self.is_one_or_zero(self.piece[4])
            and self.piece[5] == "{"
        )

    def is_many2one(self):
        return (
            self.piece[0] == "}"
            and self.is_one_or_zero(self.piece[1])
            and self.is_one_or_zero(self.piece[4])
            and self.piece[5] == "|"
        )


class RelationshipItem:
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
        self.expression = RelationshipExpression(expression)
        self.description = memo.strip('"')

    def parse(self):
        if self.expression.is_many2one():
            (
                left,
                right,
            ) = self.leaf
            self.leaf = (
                right,
                left,
            )
            self.type = "one2many"
        if self.expression.is_one2many():
            self.type = "one2many"
        if self.expression.is_one2one():
            self.type = "one2one"
        if self.expression.is_many2many():
            self.type = "many2many"

    def is_blongs_to_entity_name(self, entity_name):
        return entity_name == self.leaf[0] or entity_name == self.leaf[1]

    def __str__(self):
        return "{} {} {}".format(self.leaf[0], self.leaf[1], self.type)


class RelationshipSet:
    ALL_ENTITIES_NAME = set()

    def __init__(self, all=[]):
        self.cardinalities = set(all)
        for items in all:
            self.ALL_ENTITIES_NAME.add(items.leaf[0])
            self.ALL_ENTITIES_NAME.add(items.leaf[1])

    @staticmethod
    def is_many2many(e: RelationshipItem):
        return e.type == "many2many"

    @staticmethod
    def is_one2many(e: RelationshipItem):
        return e.type == "one2many"

    @staticmethod
    def is_one2one(e: RelationshipItem):
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

    def get_many2many_all(self):
        return list(filter(self.is_many2many, list(self.cardinalities)))

    def get_one2many_all(self):
        return list(filter(self.is_one2many, list(self.cardinalities)))

    def get_one2one_all(self):
        return list(filter(self.is_one2one, list(self.cardinalities)))

    def get_many2many_by_entity_name(self, entity_name):
        cset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_many2many, cset))

    def get_one2many_by_entity_name(self, entity_name):
        cset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_one2many, cset))

    def get_one2one_by_entity_name(self, entity_name):
        cset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_one2one, cset))
