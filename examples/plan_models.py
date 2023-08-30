from django.db import models


class Series(models.Model):
    """ series 正シリーズと番外シリーズは、別々に登録する ※巻数が自然数の順列になる [リソース]
    """

    """author 著者名 """
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
    """rel_series_id 関係するシリーズ（単方向リスト） """
    rel_series_id = models.PositiveIntegerField(
        verbose_name="関係するシリーズ（単方向リスト）",
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
    """site 代表（公式）サイト 公式サイトや他のWebサイトから代表するものを1件"""
    site = models.URLField(
        verbose_name="代表（公式）サイト",
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
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """number  第n巻"""
    number = models.PositiveIntegerField(
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
    """series  series comic"""
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

    """cw_published  """
    cw_published = models.DateField(
        null=True
    )
    """cw_url Comic Walker """
    cw_url = models.URLField(
        verbose_name="Comic Walker",
        null=True,
        blank=True
    )
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """nico_published  """
    nico_published = models.DateField(
        null=True
    )
    """nico_url ニコニコ静画 """
    nico_url = models.URLField(
        verbose_name="ニコニコ静画",
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
    """story  story web_comic"""
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

    """cover_image  """
    cover_image = models.URLField(
        null=True,
        blank=True
    )
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """released 発売日 書店等での発売日 ※タイトルの月の2か月前27日前後"""
    released = models.DateField(
        verbose_name="発売日",
        null=True
    )
    """site  """
    site = models.URLField(
        null=True,
        blank=True
    )
    """tag_line 表紙や付録になった号、などを表すタグ """
    tag_line = models.CharField(
        verbose_name="表紙や付録になった号、などを表すタグ",
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


class Fragment(models.Model):
    """ fragment その他媒体 表紙カラー、店舗特典、ポスター。コミック収録と未収録がある [リソース]
    """

    """character  character fragment"""
    character = models.ManyToManyField(
        "Character",
        related_name="fragment",
    )
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """place  place fragment"""
    place = models.ForeignKey(
        "Place",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """story  story fragment"""
    story = models.ForeignKey(
        "Story",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """title  """
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """url  """
    url = models.URLField(
        null=True,
        blank=True
    )
    """web_comic  web_comic fragment"""
    web_comic = models.ForeignKey(
        "Web_comic",
        related_name="fragment",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Journey(models.Model):
    """ journey 第〇旅、番外旅 [イベント]
    """

    """key  """
    key = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """number  """
    number = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    """type タイプ 1:本編 2:番外旅 9:その他"""
    type = models.PositiveIntegerField(
        verbose_name="タイプ",
        null=True,
        blank=True
    )


class Story(models.Model):
    """ story 単行本の単話 第〇旅前編、第〇旅後編。コミック未収録もある [イベント]
    """

    """camera_center_place  place story このストーリーに登場する主な地点をすべて包含するような範囲（四角形）の中心"""
    camera_center_place = models.ForeignKey(
        "Place",
        related_name="camera_center_place",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """camera_zoom_level  """
    camera_zoom_level = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    """comic  comic story"""
    comic = models.ForeignKey(
        "Comic",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """journey  journey story"""
    journey = models.ForeignKey(
        "Journey",
        related_name="story",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """magazine  magazine story"""
    magazine = models.OneToOneField(
        "Magazine",
        related_name="story",
        null=True,
        on_delete=models.CASCADE
    )
    """subtitle  """
    subtitle = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """title  """
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )


class Route(models.Model):
    """ route 経路 placeを組み合わせて経路とする [リソース]
    """

    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """story  story route"""
    story = models.ManyToManyField(
        "Story",
        related_name="route",
    )


class Venue(models.Model):
    """ venue 目的地 会津、松島、那須、… [リソース]
    """

    """comic  comic venue"""
    comic = models.ManyToManyField(
        "Comic",
        related_name="venue",
    )
    """name  """
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """story  story venue"""
    story = models.ManyToManyField(
        "Story",
        related_name="venue",
    )
    """type  1:都道府県 2:市区町村 3:番地等の細かい行政界 5:著名観光地 6:ランドマーク、顕著な建造物、施設 7:道、航路、等"""
    type = models.PositiveIntegerField(
        null=True,
        blank=True
    )


class Place(models.Model):
    """ place 場所 東京駅の顔出しパネル、登場店舗、宿泊場所、観光名所、施設、交通拠点 [リソース]
    """

    """altitude  """
    altitude = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """character  character place"""
    character = models.ManyToManyField(
        "Character",
        related_name="place",
    )
    """latitude  """
    latitude = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """longitude  """
    longitude = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """story  story place"""
    story = models.ManyToManyField(
        "Story",
        related_name="place",
    )
    """venue  venue place"""
    venue = models.ForeignKey(
        "Venue",
        related_name="place",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Step(models.Model):
    """ step 訪問 [イベント]
    """

    """datetime  """
    datetime = models.DateTimeField(
        null=True
    )
    """number  """
    number = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    """place  place step"""
    place = models.ForeignKey(
        "Place",
        related_name="step",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """route  route step"""
    route = models.ForeignKey(
        "Route",
        related_name="step",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Scene(models.Model):
    """ scene シーン 名シーン、ざつ旅ARのマーカー [イベント]
    """

    """character  character scene"""
    character = models.ManyToManyField(
        "Character",
        related_name="scene",
    )
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """page ページ コミック掲載ページ"""
    page = models.PositiveIntegerField(
        verbose_name="ページ",
        null=True,
        blank=True
    )
    """place  place scene"""
    place = models.ForeignKey(
        "Place",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """story  story scene"""
    story = models.ForeignKey(
        "Story",
        related_name="scene",
        null=True,
        on_delete=models.DO_NOTHING
    )


class Character(models.Model):
    """ character キャラクター 主要5人、編集部、他 [リソース]
    """

    """description  """
    description = models.TextField(
        null=True,
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """type  """
    type = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )


class Photo(models.Model):
    """ photo flickr (google place photo api有料) [リソース]
    """

    """height  """
    height = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    """place  place photo"""
    place = models.ForeignKey(
        "Place",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """url  """
    url = models.URLField(
        null=True,
        blank=True
    )
    """user  user photo"""
    user = models.ForeignKey(
        "User",
        related_name="photo",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """width  """
    width = models.PositiveIntegerField(
        null=True,
        blank=True
    )


class Tweet(models.Model):
    """ tweet Twitter 石坂さん、鈴ヶ森さん、読者等、無関係 [リソース]
    """

    """description  """
    description = models.TextField(
        null=True,
        blank=True
    )
    """place  place tweet"""
    place = models.ForeignKey(
        "Place",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING
    )
    """type  """
    type = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    """url  """
    url = models.URLField(
        null=True,
        blank=True
    )
    """user  user tweet"""
    user = models.ForeignKey(
        "User",
        related_name="tweet",
        null=True,
        on_delete=models.DO_NOTHING
    )


class User(models.Model):
    """ user ユーザー 利用者 [リソース]
    """

    """group  group user"""
    group = models.ManyToManyField(
        "Group",
        related_name="user",
    )
    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """type  """
    type = models.PositiveIntegerField(
        null=True,
        blank=True
    )


class Group(models.Model):
    """ group グループ [リソース]
    """

    """memo  """
    memo = models.TextField(
        null=True,
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    """visibility  """
    visibility = models.PositiveIntegerField(
        null=True,
        blank=True
    )
