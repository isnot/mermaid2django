from django.db import models


class Series(models.Model):
    class Meta:
        db_table_comment = "series 正シリーズと番外シリーズは、別々に登録する ※巻数が自然数の順列になる [リソース]"
        # ordering = []
        # get_latest_by = []

    author = models.CharField(
        verbose_name="著者名",
        help_text="著者複数名の場合は、代表者をカンマ区切りで列挙する",
        max_length=255,
        null=True,
        blank=True,
    )
    label = models.CharField(
        verbose_name="レーベル",
        help_text="コミック・シリーズのレーベル名称 例：電撃コミックスNEXT",
        max_length=255,
        null=True,
        blank=True,
    )
    magazine_title = models.CharField(
        verbose_name="連載誌",
        help_text="雑誌連載の誌名か、Web連載のレーベル名称",
        max_length=255,
        null=True,
        blank=True,
    )
    publisher = models.CharField(
        verbose_name="出版社",
        help_text="出版社 例：KADOKAWA",
        max_length=255,
        null=True,
        blank=True,
    )
    rel_series_id = models.PositiveIntegerField(
        verbose_name="関係シリーズ",
        help_text="モデルにはあえてリレーションを定義せず (単方向リスト)",
        null=True,
        blank=True,
    )
    short_title = models.CharField(
        verbose_name="略称",
        help_text="略称や通称で代表的なもの",
        max_length=255,
        null=True,
        blank=True,
    )
    site = models.URLField(
        verbose_name="代表(公式)サイト",
        help_text="公式サイトや他のWebサイトから代表するものを1件",
        null=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name="作品名",
        help_text="正確な作品の名称",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.title)


class Comic(models.Model):
    class Meta:
        db_table_comment = "comic 単行本 1巻、2巻、…。単巻のみの場合はseries=NULL [リソース]"
        # ordering = []
        # get_latest_by = []

    cover_image = models.URLField(
        verbose_name="書影url",
        help_text="版元ドットコムの書誌情報DBより",
        null=True,
        blank=True,
    )
    isbn = models.CharField(
        verbose_name="ISBN13",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    issued = models.DateField(
        verbose_name="発行日",
        help_text="巻末の奥付にある、初版発行日",
        null=True,
    )
    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    number = models.PositiveIntegerField(
        verbose_name="巻数",
        help_text="第n巻 入力するのは数字のみ",
        null=True,
        blank=True,
    )
    obi = models.CharField(
        verbose_name="オビ",
        help_text="特徴的な帯の文言",
        max_length=255,
        null=True,
        blank=True,
    )
    released = models.DateField(
        verbose_name="書店発売日",
        help_text="",
        null=True,
    )
    series = models.ForeignKey(
        "Series",
        help_text="",
        related_name="comic",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(
        verbose_name="各巻タイトル",
        help_text="例：ざつ旅-That's Journey- 1。※巻数の表記は作品毎に呼び方のバリエーションがある",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.title)


class Web_comic(models.Model):
    class Meta:
        db_table_comment = "web_comic Web連載 第1旅(1)、番外旅、一枚モノ、… [リソース]"
        # ordering = []
        # get_latest_by = []

    cw_published = models.DateField(
        verbose_name="CW公開日",
        help_text="",
        null=True,
    )
    cw_url = models.URLField(
        verbose_name="Comic Walkerリンク",
        help_text="",
        null=True,
        blank=True,
    )
    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    nico_published = models.DateField(
        verbose_name="nico公開日",
        help_text="",
        null=True,
    )
    nico_url = models.URLField(
        verbose_name="ニコニコ静画リンク",
        help_text="",
        null=True,
        blank=True,
    )
    pages = models.PositiveIntegerField(
        verbose_name="ページ数",
        help_text="",
        null=True,
        blank=True,
    )
    part_number = models.PositiveIntegerField(
        verbose_name="分割の順列",
        help_text="",
        null=True,
        blank=True,
    )
    story = models.ForeignKey(
        "Story",
        help_text="",
        related_name="web_comic",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(
        verbose_name="各話の名前",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.title)


class Magazine(models.Model):
    class Meta:
        db_table_comment = "magazine 雑誌連載 マオウ [イベント]"
        # ordering = []
        # get_latest_by = []

    cover_image = models.URLField(
        verbose_name="雑誌表紙",
        help_text="例: https://dengekimaoh.jp/archives/008/202208/xxxxxxxx.jpg",
        null=True,
        blank=True,
    )
    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    released = models.DateField(
        verbose_name="発売日",
        help_text="書店等での発売日 ※タイトルの月の2か月前27日前後",
        null=True,
    )
    site = models.URLField(
        verbose_name="雑誌リンク",
        help_text="例: https://dengekimaoh.jp/magazine/magazine-nnnnn.html",
        null=True,
        blank=True,
    )
    tag_line = models.CharField(
        verbose_name="管理用タグ",
        help_text="表紙や付録になった号、などを表すタグ",
        max_length=255,
        null=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name="タイトル",
        help_text="雑誌のタイトル 例：電撃マオウ 2020年1月号",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.title)


class Type_master(models.Model):
    class Meta:
        db_table_comment = "type_master 分類型の項目の選択肢マスター [リソース]"
        # ordering = []
        # get_latest_by = []

    key = models.CharField(
        verbose_name="属性",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name="参照名",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    value = models.CharField(
        verbose_name="値",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.name)


class Fragment(models.Model):
    class Meta:
        db_table_comment = "fragment その他媒体 表紙カラー、店舗特典、ポスター、別冊、雑誌付録。コミック収録と未収録がある [リソース]"
        # ordering = []
        # get_latest_by = []

    character = models.ManyToManyField(
        "Character",
        help_text="",
        related_name="fragment",
    )
    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    place = models.ForeignKey(
        "Place",
        help_text="",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    story = models.ForeignKey(
        "Story",
        help_text="",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(
        verbose_name="名前",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master fragment",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    url = models.URLField(
        verbose_name="参照URL/リンク",
        help_text="",
        null=True,
        blank=True,
    )
    web_comic = models.ForeignKey(
        "Web_comic",
        help_text="",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.title)


class Journey(models.Model):
    class Meta:
        db_table_comment = "journey 第〇旅、番外旅 [イベント]"
        # ordering = []
        # get_latest_by = []

    key = models.CharField(
        verbose_name="記号",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    number = models.PositiveIntegerField(
        verbose_name="第〇旅",
        help_text="入力は数字のみ",
        null=True,
        blank=True,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master journey",
        related_name="journey",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.pk)


class Story(models.Model):
    class Meta:
        db_table_comment = "story 単行本の単話 第〇旅前編、第〇旅後編。コミック未収録もある [イベント]"
        # ordering = []
        # get_latest_by = []

    camera_center_place = models.ForeignKey(
        "Place",
        verbose_name="(領域設定用)",
        help_text="place story このストーリーに登場する主な地点をすべて包含するような範囲(四角形)の中心",
        related_name="camera_center_place",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    camera_zoom_level = models.PositiveIntegerField(
        verbose_name="(領域設定用)zoom",
        help_text="",
        null=True,
        blank=True,
    )
    comic = models.ForeignKey(
        "Comic",
        help_text="",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    journey = models.ForeignKey(
        "Journey",
        help_text="",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    magazine = models.OneToOneField(
        "Magazine",
        help_text="",
        related_name="story",
        null=True,
        on_delete=models.CASCADE,
    )
    subtitle = models.CharField(
        verbose_name="サブタイトル",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name="単話タイトル",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master story",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.title)


class Route(models.Model):
    class Meta:
        db_table_comment = "route 経路 placeを組み合わせて経路とする [リソース]"
        # ordering = []
        # get_latest_by = []

    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name="名前",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    story = models.ManyToManyField(
        "Story",
        help_text="",
        related_name="route",
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master route",
        related_name="route",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.name)


class Venue(models.Model):
    class Meta:
        db_table_comment = "venue 目的地 会津、松島、那須、… [リソース]"
        # ordering = []
        # get_latest_by = []

    name = models.CharField(
        verbose_name="名称",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    story = models.ManyToManyField(
        "Story",
        help_text="",
        related_name="venue",
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master venue",
        related_name="venue",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.name)


class Place(models.Model):
    class Meta:
        db_table_comment = "place 場所 東京駅の顔出しパネル、登場店舗、宿泊場所、観光名所、施設、交通拠点 [リソース]"
        # ordering = []
        # get_latest_by = []

    address = models.CharField(
        verbose_name="住所",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    altitude = models.DecimalField(
        verbose_name="高度",
        help_text="",
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    latitude = models.DecimalField(
        verbose_name="緯度",
        help_text="",
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        verbose_name="経度",
        help_text="",
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name="地点名",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    venue = models.ForeignKey(
        "Venue",
        help_text="",
        related_name="place",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.name)


class Step(models.Model):
    class Meta:
        db_table_comment = "step 訪問 routeに含まれる地点を訪れた日時 [イベント]"
        # ordering = []
        # get_latest_by = []

    datetime = models.DateTimeField(
        verbose_name="日時",
        help_text="",
        null=True,
    )
    number = models.PositiveIntegerField(
        verbose_name="順番",
        help_text="",
        null=True,
        blank=True,
    )
    place = models.ForeignKey(
        "Place",
        help_text="",
        related_name="step",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    route = models.ForeignKey(
        "Route",
        help_text="",
        related_name="step",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.pk)


class Scene(models.Model):
    class Meta:
        db_table_comment = "scene シーン 名シーン、ざつ旅ARのマーカー [イベント]"
        # ordering = []
        # get_latest_by = []

    character = models.ManyToManyField(
        "Character",
        help_text="",
        related_name="scene",
    )
    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    page = models.PositiveIntegerField(
        verbose_name="ページ",
        help_text="コミック掲載ページ",
        null=True,
        blank=True,
    )
    place = models.ForeignKey(
        "Place",
        help_text="",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    story = models.ForeignKey(
        "Story",
        help_text="",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master scene",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.pk)


class Character(models.Model):
    class Meta:
        db_table_comment = "character キャラクター 主要5人、編集部、他 [リソース]"
        # ordering = []
        # get_latest_by = []

    description = models.TextField(
        verbose_name="紹介文",
        help_text="",
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name="名前",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master character",
        related_name="character",
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return "{0}".format(self.name)


class Photo(models.Model):
    class Meta:
        db_table_comment = "photo flickr (google place photo api有料) [リソース]"
        # ordering = []
        # get_latest_by = []

    height = models.PositiveIntegerField(
        verbose_name="画像高さ",
        help_text="",
        null=True,
        blank=True,
    )
    image_src = models.URLField(
        verbose_name="画像URL",
        help_text="",
        null=True,
        blank=True,
    )
    link = models.URLField(
        verbose_name="参照ページURL",
        help_text="",
        null=True,
        blank=True,
    )
    person = models.ForeignKey(
        "Person",
        help_text="",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    step = models.ForeignKey(
        "Step",
        help_text="",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(
        verbose_name="タイトル",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master photo",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    username = models.CharField(
        verbose_name="撮影者",
        help_text="参照先固有の、撮影者を識別する情報",
        max_length=255,
        null=True,
        blank=True,
    )
    width = models.PositiveIntegerField(
        verbose_name="画像幅",
        help_text="",
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.title)


class Tweet(models.Model):
    class Meta:
        db_table_comment = "tweet Twitter 石坂さん、鈴ヶ森さん、読者等、無関係 [リソース]"
        # ordering = []
        # get_latest_by = []

    description = models.TextField(
        verbose_name="内容",
        help_text="",
        null=True,
        blank=True,
    )
    person = models.ForeignKey(
        "Person",
        help_text="",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    step = models.ForeignKey(
        "Step",
        help_text="",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    tweet_id = models.CharField(
        verbose_name="Tweet ID",
        help_text="桁数が大きいため、JSON等では数値型で扱えないことに注意",
        max_length=255,
        null=True,
        blank=True,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master tweet",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    url = models.URLField(
        verbose_name="固定URL",
        help_text="",
        null=True,
        blank=True,
    )
    username = models.CharField(
        verbose_name="ツイ主の@username",
        help_text="@username は変わる可能性があることに注意",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.pk)


class Person(models.Model):
    class Meta:
        db_table_comment = "person コンテンツの作者 ツイート/写真を撮影した人 [リソース]"
        # ordering = []
        # get_latest_by = []

    memo = models.TextField(
        verbose_name="編集メモ",
        help_text="",
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name="名前",
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        help_text="type_master person",
        related_name="person",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    user = models.OneToOneField(
        "User",
        help_text="",
        related_name="person",
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0}".format(self.name)


class User(models.Model):
    class Meta:
        db_table_comment = "user ユーザー 利用者 [リソース]"
        # ordering = []
        # get_latest_by = []

    date_joined = models.DateTimeField(
        help_text="",
        null=True,
    )
    email = models.CharField(
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )
    username = models.CharField(
        help_text="",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{0}".format(self.pk)
