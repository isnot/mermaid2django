from django.db import models


class Series(models.Model):
    """ series 正シリーズと番外シリーズは、別々に登録する ※巻数が自然数の順列になる [リソース]
    """

    """author 著者名 著者複数名の場合は、代表者をカンマ区切りで列挙する"""
    author = models.CharField(
        verbose_name="著者名",
        max_length=255,
        null=True,
        blank=True
    )
    """label レーベル コミック・シリーズのレーベル名称 例：電撃コミックスNEXT"""
    label = models.CharField(
        verbose_name="レーベル",
        max_length=255,
        null=True,
        blank=True
    )
    """magazine_title 連載誌 雑誌連載の誌名か、Web連載のレーベル名称"""
    magazine_title = models.CharField(
        verbose_name="連載誌",
        max_length=255,
        null=True,
        blank=True
    )
    """publisher 出版社 出版社 例：KADOKAWA"""
    publisher = models.CharField(
        verbose_name="出版社",
        max_length=255,
        null=True,
        blank=True
    )
    """rel_series_id 関係シリーズ モデルにはあえてリレーションを定義せず (単方向リスト)"""
    rel_series_id = models.PositiveIntegerField(
        verbose_name="関係シリーズ",
        null=True,
        blank=True
    )
    """short_title 略称 略称や通称で代表的なもの"""
    short_title = models.CharField(
        verbose_name="略称",
        max_length=255,
        null=True,
        blank=True
    )
    """site 代表(公式)サイト 公式サイトや他のWebサイトから代表するものを1件"""
    site = models.URLField(
        verbose_name="代表(公式)サイト",
        null=True,
        blank=True
    )
    """title 作品名 正確な作品の名称"""
    title = models.CharField(
        verbose_name="作品名",
        max_length=255,
        null=True,
        blank=True
    )


class Comic(models.Model):
    """ comic 単行本 1巻、2巻、…。単巻のみの場合はseries=NULL [リソース]
    """

    """cover_image_url 書影url 版元ドットコムの書誌情報DBより"""
    cover_image_url = models.URLField(
        verbose_name="書影url",
        null=True,
        blank=True
    )
    """isbn ISBN13 """
    isbn = models.CharField(
        verbose_name="ISBN13",
        max_length=255,
        null=True,
        blank=True
    )
    """issued 発行日 巻末の奥付にある、初版発行日"""
    issued = models.DateField(
        verbose_name="発行日",
        null=True
    )
    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """number 巻数 第n巻 作品毎に呼び方のバリエーションがある"""
    number = models.PositiveIntegerField(
        verbose_name="巻数",
        null=True,
        blank=True
    )
    """obi オビ 特徴的な帯の文言"""
    obi = models.CharField(
        verbose_name="オビ",
        max_length=255,
        null=True,
        blank=True
    )
    """released 書店発売日 """
    released = models.DateField(
        verbose_name="書店発売日",
        null=True
    )
    """series  """
    series = models.ForeignKey(
        "Series",
        related_name="comic",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """title 各巻タイトル 例：ざつ旅-That's Journey- 1"""
    title = models.CharField(
        verbose_name="各巻タイトル",
        max_length=255,
        null=True,
        blank=True
    )


class Web_comic(models.Model):
    """ web_comic Web連載 第1旅(1)、番外旅、一枚モノ、… [リソース]
    """

    """cw_published CW公開日 """
    cw_published = models.DateField(
        verbose_name="CW公開日",
        null=True
    )
    """cw_url Comic Walkerリンク """
    cw_url = models.URLField(
        verbose_name="Comic Walkerリンク",
        null=True,
        blank=True
    )
    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """nico_published nico公開日 """
    nico_published = models.DateField(
        verbose_name="nico公開日",
        null=True
    )
    """nico_url ニコニコ静画リンク """
    nico_url = models.URLField(
        verbose_name="ニコニコ静画リンク",
        null=True,
        blank=True
    )
    """pages ページ数 """
    pages = models.PositiveIntegerField(
        verbose_name="ページ数",
        null=True,
        blank=True
    )
    """part_number 分割の順列 """
    part_number = models.PositiveIntegerField(
        verbose_name="分割の順列",
        null=True,
        blank=True
    )
    """story  """
    story = models.ForeignKey(
        "Story",
        related_name="web_comic",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """title 各話の名前 """
    title = models.CharField(
        verbose_name="各話の名前",
        max_length=255,
        null=True,
        blank=True
    )


class Magazine(models.Model):
    """ magazine 雑誌連載 マオウ [イベント]
    """

    """cover_image 雑誌表紙 https://dengekimaoh.jp/archives/008/202208/941abdc5a8102a20bb186ae99e37f234c96e5209270d10b52c0293a2419db042.jpg"""
    cover_image = models.URLField(
        verbose_name="雑誌表紙",
        null=True,
        blank=True
    )
    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """released 発売日 書店等での発売日 ※タイトルの月の2か月前27日前後"""
    released = models.DateField(
        verbose_name="発売日",
        null=True
    )
    """site 雑誌リンク https://dengekimaoh.jp/magazine/magazine-12240.html"""
    site = models.URLField(
        verbose_name="雑誌リンク",
        null=True,
        blank=True
    )
    """tag_line 管理用タグ 表紙や付録になった号、などを表すタグ"""
    tag_line = models.CharField(
        verbose_name="管理用タグ",
        max_length=255,
        null=True,
        blank=True
    )
    """title タイトル 雑誌のタイトル 例：電撃マオウ 2020年1月号"""
    title = models.CharField(
        verbose_name="タイトル",
        max_length=255,
        null=True,
        blank=True
    )


class Type_master(models.Model):
    """ type_master 分類型の項目の選択肢マスター [リソース]
    """

    """key 属性 """
    key = models.CharField(
        verbose_name="属性",
        max_length=255,
        null=True,
        blank=True
    )
    """name 参照名 """
    name = models.CharField(
        verbose_name="参照名",
        max_length=255,
        null=True,
        blank=True
    )
    """value 値 """
    value = models.CharField(
        verbose_name="値",
        max_length=255,
        null=True,
        blank=True
    )


class Fragment(models.Model):
    """ fragment その他媒体 表紙カラー、店舗特典、ポスター、別冊、雑誌付録。コミック収録と未収録がある [リソース]
    """

    """character  """
    character = models.ManyToManyField(
        "Character",
        related_name="fragment",
    )
    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """place  """
    place = models.ForeignKey(
        "Place",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """story  """
    story = models.ForeignKey(
        "Story",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """title 名前 """
    title = models.CharField(
        verbose_name="名前",
        max_length=255,
        null=True,
        blank=True
    )
    """type_master 分類 種別 """
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類 種別",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """url 参照URL/リンク """
    url = models.URLField(
        verbose_name="参照URL/リンク",
        null=True,
        blank=True
    )
    """web_comic  """
    web_comic = models.ForeignKey(
        "Web_comic",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Journey(models.Model):
    """ journey 第〇旅、番外旅 [イベント]
    """

    """key 記号 """
    key = models.CharField(
        verbose_name="記号",
        max_length=255,
        null=True,
        blank=True
    )
    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """number 第〇旅 """
    number = models.PositiveIntegerField(
        verbose_name="第〇旅",
        null=True,
        blank=True
    )
    """type_master 分類 type_master 1:本編 2:番外旅 9:その他 ToDo"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="journey",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Story(models.Model):
    """ story 単行本の単話 第〇旅前編、第〇旅後編。コミック未収録もある [イベント]
    """

    """camera_center_place (領域設定用) place story このストーリーに登場する主な地点をすべて包含するような範囲(四角形)の中心"""
    camera_center_place = models.ForeignKey(
        "Place",
        verbose_name="(領域設定用)",
        related_name="camera_center_place",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """camera_zoom_level (領域設定用)zoom """
    camera_zoom_level = models.PositiveIntegerField(
        verbose_name="(領域設定用)zoom",
        null=True,
        blank=True
    )
    """comic  """
    comic = models.ForeignKey(
        "Comic",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """journey  """
    journey = models.ForeignKey(
        "Journey",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """magazine  """
    magazine = models.OneToOneField(
        "Magazine",
        related_name="story",
        null=True,
        on_delete=models.CASCADE
    )
    """subtitle サブタイトル """
    subtitle = models.CharField(
        verbose_name="サブタイトル",
        max_length=255,
        null=True,
        blank=True
    )
    """title 単話タイトル """
    title = models.CharField(
        verbose_name="単話タイトル",
        max_length=255,
        null=True,
        blank=True
    )
    """type_master 分類 type_master 本編、番外旅、おうちで料理 ToDo"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Route(models.Model):
    """ route 経路 placeを組み合わせて経路とする [リソース]
    """

    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """name 名前 """
    name = models.CharField(
        verbose_name="名前",
        max_length=255,
        null=True,
        blank=True
    )
    """story  """
    story = models.ManyToManyField(
        "Story",
        related_name="route",
    )
    """type_master 分類 type_master 鈴ヶ森さんツイ、作者、マップ取り込み、調整済 ToDo"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="route",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Venue(models.Model):
    """ venue 目的地 会津、松島、那須、… [リソース]
    """

    """comic  """
    comic = models.ManyToManyField(
        "Comic",
        related_name="venue",
    )
    """name 名称 """
    name = models.CharField(
        verbose_name="名称",
        max_length=255,
        null=True,
        blank=True
    )
    """story  """
    story = models.ManyToManyField(
        "Story",
        related_name="venue",
    )
    """type_master 分類 type_master 1:都道府県 2:市区町村 3:番地等の細かい行政界 5:著名観光地 6:ランドマーク、顕著な建造物、施設 7:道、航路、等"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="venue",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Place(models.Model):
    """ place 場所 東京駅の顔出しパネル、登場店舗、宿泊場所、観光名所、施設、交通拠点 [リソース]
    """

    """altitude 高度 """
    altitude = models.CharField(
        verbose_name="高度",
        max_length=255,
        null=True,
        blank=True
    )
    """character  """
    character = models.ManyToManyField(
        "Character",
        related_name="place",
    )
    """latitude 緯度 """
    latitude = models.CharField(
        verbose_name="緯度",
        max_length=255,
        null=True,
        blank=True
    )
    """longitude 経度 """
    longitude = models.CharField(
        verbose_name="経度",
        max_length=255,
        null=True,
        blank=True
    )
    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """name 地点名 """
    name = models.CharField(
        verbose_name="地点名",
        max_length=255,
        null=True,
        blank=True
    )
    """story  """
    story = models.ManyToManyField(
        "Story",
        related_name="place",
    )
    """venue  """
    venue = models.ForeignKey(
        "Venue",
        related_name="place",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Step(models.Model):
    """ step 訪問 routeに含まれる地点を訪れた日時 [イベント]
    """

    """datetime 日時 """
    datetime = models.DateTimeField(
        verbose_name="日時",
        null=True
    )
    """number 順番 """
    number = models.PositiveIntegerField(
        verbose_name="順番",
        null=True,
        blank=True
    )
    """place  """
    place = models.ForeignKey(
        "Place",
        related_name="step",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """route  """
    route = models.ForeignKey(
        "Route",
        related_name="step",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Scene(models.Model):
    """ scene シーン 名シーン、ざつ旅ARのマーカー [イベント]
    """

    """character  """
    character = models.ManyToManyField(
        "Character",
        related_name="scene",
    )
    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """page ページ コミック掲載ページ"""
    page = models.PositiveIntegerField(
        verbose_name="ページ",
        null=True,
        blank=True
    )
    """place  """
    place = models.ForeignKey(
        "Place",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """story  """
    story = models.ForeignKey(
        "Story",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """type_master 分類 """
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Character(models.Model):
    """ character キャラクター 主要5人、編集部、他 [リソース]
    """

    """description 紹介文 """
    description = models.TextField(
        verbose_name="紹介文",
        null=True,
        blank=True
    )
    """name 名前 """
    name = models.CharField(
        verbose_name="名前",
        max_length=255,
        null=True,
        blank=True
    )
    """type_master 分類 type_master character ToDo"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="character",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Photo(models.Model):
    """ photo flickr (google place photo api有料) [リソース]
    """

    """height 画像高さ """
    height = models.PositiveIntegerField(
        verbose_name="画像高さ",
        null=True,
        blank=True
    )
    """person  """
    person = models.ForeignKey(
        "Person",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """step  """
    step = models.ForeignKey(
        "Step",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """title タイトル """
    title = models.CharField(
        verbose_name="タイトル",
        max_length=255,
        null=True,
        blank=True
    )
    """type_master 分類 type_master photo 出典別？ ToDo"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """url 参照URL """
    url = models.URLField(
        verbose_name="参照URL",
        null=True,
        blank=True
    )
    """width 画像幅 """
    width = models.PositiveIntegerField(
        verbose_name="画像幅",
        null=True,
        blank=True
    )


class Tweet(models.Model):
    """ tweet Twitter 石坂さん、鈴ヶ森さん、読者等、無関係 [リソース]
    """

    """description 内容 """
    description = models.TextField(
        verbose_name="内容",
        null=True,
        blank=True
    )
    """person  """
    person = models.ForeignKey(
        "Person",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """step  """
    step = models.ForeignKey(
        "Step",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """type_master 分類 type_master tweet 鈴ヶ森さん、作者、巡礼・追走、 ToDo"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """url 固定URL """
    url = models.URLField(
        verbose_name="固定URL",
        null=True,
        blank=True
    )


class Person(models.Model):
    """ person コンテンツの作者 ツイート/写真を撮影した人 [リソース]
    """

    """memo 編集メモ """
    memo = models.TextField(
        verbose_name="編集メモ",
        null=True,
        blank=True
    )
    """name 名前 """
    name = models.CharField(
        verbose_name="名前",
        max_length=255,
        null=True,
        blank=True
    )
    """type_master 分類 type_master person ToDo"""
    type_master = models.ForeignKey(
        "Type_master",
        verbose_name="分類",
        related_name="person",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """user  """
    user = models.OneToOneField(
        "User",
        related_name="person",
        null=True,
        on_delete=models.CASCADE
    )


class User(models.Model):
    """ user ユーザー 利用者 [リソース]
    """

    """date_joined  """
    date_joined = models.DateTimeField(
        null=True
    )
    """email  """
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """first_name  """
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """last_name  """
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """username  """
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
