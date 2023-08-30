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
    def __init__(self, items=[], annotation=""):
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
        self.annotation = annotation

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
        self.attribute_name = self.annotation.split(" ")[0]

    def is_blongs_to_entity_name(self, entity_name):
        return entity_name == self.leaf[0] or entity_name == self.leaf[1]

    def __str__(self):
        return "{} {} {} {}".format(
            self.leaf[0], self.leaf[1], self.type, self.annotation
        )


class RelationshipSet:
    ALL_ENTITY_NAMES = set()

    def __init__(self, all=[]):
        self.relations = set(all)
        for items in all:
            self.ALL_ENTITY_NAMES.add(items.leaf[0])
            self.ALL_ENTITY_NAMES.add(items.leaf[1])

    @staticmethod
    def is_many2many(e: RelationshipItem):
        return e.type == "many2many"

    @staticmethod
    def is_one2many(e: RelationshipItem):
        return e.type == "one2many"

    @staticmethod
    def is_one2one(e: RelationshipItem):
        return e.type == "one2one"

    def get_relations(self):
        return self.relations

    def is_link_table(self, entity_name=""):
        tmp = entity_name.partition("__")
        if tmp[1] == "" and tmp[2] == "":
            return False
        return tmp[0] in self.ALL_ENTITY_NAMES and tmp[2] in self.ALL_ENTITY_NAMES

    def is_valid_entity_name(self, name):
        return name in self.ALL_ENTITY_NAMES

    def find_by_entity_name(self, entity_name):
        if entity_name not in self.ALL_ENTITY_NAMES:
            raise RuntimeError("unkown entity name")
        found = []
        for item in self.relations:
            if item.is_blongs_to_entity_name(entity_name):
                found.append(item)
        return found

    def get_many2many_all(self):
        return list(filter(self.is_many2many, list(self.relations)))

    def get_one2many_all(self):
        return list(filter(self.is_one2many, list(self.relations)))

    def get_one2one_all(self):
        return list(filter(self.is_one2one, list(self.relations)))

    def get_many2many_by_entity_name(self, entity_name):
        myset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_many2many, myset))

    def get_one2many_by_entity_name(self, entity_name):
        myset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_one2many, myset))

    def get_one2one_by_entity_name(self, entity_name):
        myset = self.find_by_entity_name(entity_name)
        return list(filter(self.is_one2one, myset))
