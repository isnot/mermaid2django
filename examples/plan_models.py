from django.db import models


class Series(models.Model):
    """ series 正シリーズと番外シリーズは、別々に登録する ※巻数が自然数の順列になる [リソース]
    """
    """author 著者名 """
    author = models.CharField(
        verbose_name="著者名",
        max_length=255,
        blank=True
    )
    """label レーベル コミック・シリーズのレーベル名称 例：電撃コミックスNEXT"""
    label = models.CharField(
        verbose_name="レーベル",
        max_length=255,
        blank=True
    )
    """magazine_title 連載誌 雑誌連載の誌名か、Web連載のレーベル名称"""
    magazine_title = models.CharField(
        verbose_name="連載誌",
        max_length=255,
        blank=True
    )
    """publisher 出版社 出版社 例：KADOKAWA"""
    publisher = models.CharField(
        verbose_name="出版社",
        max_length=255,
        blank=True
    )
    """rel_series_id 関係するシリーズ（単方向リスト） """
    rel_series_id = models.PositiveIntegerField(
        verbose_name="関係するシリーズ（単方向リスト）",
        blank=True
    )
    """short_title 略称 略称や通称で代表的なもの"""
    short_title = models.CharField(
        verbose_name="略称",
        max_length=255,
        blank=True
    )
    """site 代表（公式）サイト 公式サイトや他のWebサイトから代表するものを1件"""
    site = models.URLField(
        verbose_name="代表（公式）サイト",
        blank=True
    )
    """title 作品名 正確な作品の名称"""
    title = models.CharField(
        verbose_name="作品名",
        max_length=255,
        blank=True
    )



class Comic(models.Model):
    """ comic 単行本 1巻、2巻、…。単巻のみの場合はseries=NULL [リソース]
    """
    """cover_image_url 書影url 版元ドットコムの書誌情報DBより"""
    cover_image_url = models.URLField(
        verbose_name="書影url",
        blank=True
    )
    """isbn ISBN13 """
    isbn = models.CharField(
        verbose_name="ISBN13",
        max_length=255,
        blank=True
    )
    """issued 発行日 巻末の奥付にある、初版発行日"""
    issued = models.DateField(
        verbose_name="発行日",
        auto_now_add=True
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """number  第n巻"""
    number = models.PositiveIntegerField(
        blank=True
    )
    """obi オビ 特徴的な帯の文言"""
    obi = models.CharField(
        verbose_name="オビ",
        max_length=255,
        blank=True
    )
    """released 書店発売日 """
    released = models.DateField(
        verbose_name="書店発売日",
        auto_now_add=True
    )
    """series  series comic one2many"""
    series = models.ForeignKey(
        "Series",
        related_name="comic",
        on_delete=models.CASCADE
    )
    """title 各巻タイトル 例：ざつ旅-That's Journey- 1"""
    title = models.CharField(
        verbose_name="各巻タイトル",
        max_length=255,
        blank=True
    )



class Web_comic(models.Model):
    """ web_comic Web連載 第1旅(1)、番外旅、一枚モノ、… [リソース]
    """
    """cw_published  """
    cw_published = models.DateField(
        auto_now_add=True
    )
    """cw_url Comic Walker """
    cw_url = models.URLField(
        verbose_name="Comic Walker",
        blank=True
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """nico_published  """
    nico_published = models.DateField(
        auto_now_add=True
    )
    """nico_url ニコニコ静画 """
    nico_url = models.URLField(
        verbose_name="ニコニコ静画",
        blank=True
    )
    """pages ページ数 """
    pages = models.PositiveIntegerField(
        verbose_name="ページ数",
        blank=True
    )
    """part_number 分割の順列 """
    part_number = models.PositiveIntegerField(
        verbose_name="分割の順列",
        blank=True
    )
    """story  story web_comic one2many"""
    story = models.ForeignKey(
        "Story",
        related_name="web_comic",
        on_delete=models.CASCADE
    )
    """title 各話の名前 """
    title = models.CharField(
        verbose_name="各話の名前",
        max_length=255,
        blank=True
    )



class Magazine(models.Model):
    """ magazine 雑誌連載 マオウ [イベント]
    """
    """cover_image  """
    cover_image = models.URLField(
        blank=True
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """released 発売日 書店等での発売日 ※タイトルの月の2か月前27日前後"""
    released = models.DateField(
        verbose_name="発売日",
        auto_now_add=True
    )
    """site  """
    site = models.URLField(
        blank=True
    )
    """tag_line 表紙や付録になった号、などを表すタグ """
    tag_line = models.CharField(
        verbose_name="表紙や付録になった号、などを表すタグ",
        max_length=255,
        blank=True
    )
    """title タイトル 雑誌のタイトル 例：電撃マオウ 2020年1月号"""
    title = models.CharField(
        verbose_name="タイトル",
        max_length=255,
        blank=True
    )



class Fragment(models.Model):
    """ fragment その他媒体 表紙カラー、店舗特典、ポスター。コミック収録と未収録がある [リソース]
    """
    """character  character fragment many2many"""
    character = models.ManyToManyField(
        "Character",
        related_name="fragment",
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """place  place fragment one2many"""
    place = models.ForeignKey(
        "Place",
        related_name="fragment",
        on_delete=models.CASCADE
    )
    """story  story fragment one2many"""
    story = models.ForeignKey(
        "Story",
        related_name="fragment",
        on_delete=models.CASCADE
    )
    """title  """
    title = models.CharField(
        max_length=255,
        blank=True
    )
    """url  """
    url = models.URLField(
        blank=True
    )
    """web_comic  web_comic fragment one2many"""
    web_comic = models.ForeignKey(
        "Web_comic",
        related_name="fragment",
        on_delete=models.CASCADE
    )



class Journey(models.Model):
    """ journey 第〇旅、番外旅 [イベント]
    """
    """key  """
    key = models.CharField(
        max_length=255,
        blank=True
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """number  """
    number = models.PositiveIntegerField(
        blank=True
    )
    """type タイプ 1:本編 2:番外旅 9:その他"""
    type = models.PositiveIntegerField(
        verbose_name="タイプ",
        blank=True
    )



class Story(models.Model):
    """ story 単行本の単話 第〇旅前編、第〇旅後編。コミック未収録もある [イベント]
    """
    """camera_center_place  place story one2many このストーリーに登場する主な地点をすべて包含するような範囲（四角形）の中心"""
    camera_center_place = models.ForeignKey(
        "Place",
        related_name="story",
        on_delete=models.CASCADE
    )
    """camera_zoom_level  """
    camera_zoom_level = models.PositiveIntegerField(
        blank=True
    )
    """comic  comic story one2many"""
    comic = models.ForeignKey(
        "Comic",
        related_name="story",
        on_delete=models.CASCADE
    )
    """journey  journey story one2many"""
    journey = models.ForeignKey(
        "Journey",
        related_name="story",
        on_delete=models.CASCADE
    )
    """magazine  magazine story one2one"""
    magazine = models.OneToOneField(
        "Magazine",
        related_name="story",
        on_delete=models.CASCADE
    )
    """subtitle  """
    subtitle = models.CharField(
        max_length=255,
        blank=True
    )
    """title  """
    title = models.CharField(
        max_length=255,
        blank=True
    )



class Route(models.Model):
    """ route 経路 placeを組み合わせて経路とする [リソース]
    """
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        blank=True
    )
    """story  story route many2many"""
    story = models.ManyToManyField(
        "Story",
        related_name="route",
    )



class Venue(models.Model):
    """ venue 目的地 会津、松島、那須、… [リソース]
    """
    """comic  comic venue many2many"""
    comic = models.ManyToManyField(
        "Comic",
        related_name="venue",
    )
    """name  """
    name = models.CharField(
        max_length=255,
        blank=True
    )
    """story  story venue many2many"""
    story = models.ManyToManyField(
        "Story",
        related_name="venue",
    )
    """type  1:都道府県 2:市区町村 3:番地等の細かい行政界 5:著名観光地 6:ランドマーク、顕著な建造物、施設 7:道、航路、等"""
    type = models.PositiveIntegerField(
        blank=True
    )



class Place(models.Model):
    """ place 場所 東京駅の顔出しパネル、登場店舗、宿泊場所、観光名所、施設、交通拠点 [リソース]
    """
    """altitude  """
    altitude = models.CharField(
        max_length=255,
        blank=True
    )
    """character  character place many2many"""
    character = models.ManyToManyField(
        "Character",
        related_name="place",
    )
    """latitude  """
    latitude = models.CharField(
        max_length=255,
        blank=True
    )
    """longitude  """
    longitude = models.CharField(
        max_length=255,
        blank=True
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        blank=True
    )
    """story  story place many2many"""
    story = models.ManyToManyField(
        "Story",
        related_name="place",
    )
    """venue  venue place one2many"""
    venue = models.ForeignKey(
        "Venue",
        related_name="place",
        on_delete=models.CASCADE
    )



class Step(models.Model):
    """ step 訪問 [イベント]
    """
    """datetime  """
    datetime = models.DatetimeField(
        auto_now_add=True
    )
    """number  """
    number = models.PositiveIntegerField(
        blank=True
    )
    """place  place step one2many"""
    place = models.ForeignKey(
        "Place",
        related_name="step",
        on_delete=models.CASCADE
    )
    """route  route step one2many"""
    route = models.ForeignKey(
        "Route",
        related_name="step",
        on_delete=models.CASCADE
    )



class Scene(models.Model):
    """ scene シーン 名シーン、ざつ旅ARのマーカー [イベント]
    """
    """character  character scene many2many"""
    character = models.ManyToManyField(
        "Character",
        related_name="scene",
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """page ページ コミック掲載ページ"""
    page = models.PositiveIntegerField(
        verbose_name="ページ",
        blank=True
    )
    """place  place scene one2many"""
    place = models.ForeignKey(
        "Place",
        related_name="scene",
        on_delete=models.CASCADE
    )
    """story  story scene one2many"""
    story = models.ForeignKey(
        "Story",
        related_name="scene",
        on_delete=models.CASCADE
    )



class Character(models.Model):
    """ character キャラクター 主要5人、編集部、他 [リソース]
    """
    """description  """
    description = models.TextField(
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        blank=True
    )
    """type  """
    type = models.CharField(
        max_length=255,
        blank=True
    )



class Photo(models.Model):
    """ photo flickr (google place photo api有料) [リソース]
    """
    """height  """
    height = models.PositiveIntegerField(
        blank=True
    )
    """place  place photo one2many"""
    place = models.ForeignKey(
        "Place",
        related_name="photo",
        on_delete=models.CASCADE
    )
    """url  """
    url = models.URLField(
        blank=True
    )
    """user  user photo one2many"""
    user = models.ForeignKey(
        "User",
        related_name="photo",
        on_delete=models.CASCADE
    )
    """width  """
    width = models.PositiveIntegerField(
        blank=True
    )



class Tweet(models.Model):
    """ tweet Twitter 石坂さん、鈴ヶ森さん、読者等、無関係 [リソース]
    """
    """description  """
    description = models.TextField(
        blank=True
    )
    """place  place tweet one2many"""
    place = models.ForeignKey(
        "Place",
        related_name="tweet",
        on_delete=models.CASCADE
    )
    """type  """
    type = models.PositiveIntegerField(
        blank=True
    )
    """url  """
    url = models.URLField(
        blank=True
    )
    """user  user tweet one2many"""
    user = models.ForeignKey(
        "User",
        related_name="tweet",
        on_delete=models.CASCADE
    )



class User(models.Model):
    """ user ユーザー 利用者 [リソース]
    """
    """group  group user many2many"""
    group = models.ManyToManyField(
        "Group",
        related_name="user",
    )
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        blank=True
    )
    """type  """
    type = models.PositiveIntegerField(
        blank=True
    )



class Group(models.Model):
    """ group グループ [リソース]
    """
    """memo  """
    memo = models.TextField(
        blank=True
    )
    """name  """
    name = models.CharField(
        max_length=255,
        blank=True
    )
    """visibility  """
    visibility = models.PositiveIntegerField(
        blank=True
    )

