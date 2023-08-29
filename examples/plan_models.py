from django.db import models
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')


class Series(models.Model):
    """ series 正シリーズと番外シリーズは、別々に登録する ※巻数が自然数の順列になる [リソース]
    """

####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'auto_now_add=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'auto_now_add=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'auto_now_add=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'auto_now_add=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')


class Comic(models.Model):
    """ comic 単行本 1巻、2巻、…。単巻のみの場合はseries=NULL [リソース]
    """

####op ['verbose_name="{verbose}"', 'auto_now_add=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'auto_now_add=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'auto_now_add=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'auto_now_add=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')


class Web_comic(models.Model):
    """ web_comic Web連載 第1旅(1)、番外旅、一枚モノ、… [リソース]
    """

####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'auto_now_add=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'auto_now_add=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')


class Magazine(models.Model):
    """ magazine 雑誌連載 マオウ [イベント]
    """

####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')


class Fragment(models.Model):
    """ fragment その他媒体 表紙カラー、店舗特典、ポスター。コミック収録と未収録がある [リソース]
    """

####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')


class Journey(models.Model):
    """ journey 第〇旅、番外旅 [イベント]
    """

####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')


class Story(models.Model):
    """ story 単行本の単話 第〇旅前編、第〇旅後編。コミック未収録もある [イベント]
    """

####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')


class Route(models.Model):
    """ route 経路 placeを組み合わせて経路とする [リソース]
    """

####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')


class Venue(models.Model):
    """ venue 目的地 会津、松島、那須、… [リソース]
    """

####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')


class Place(models.Model):
    """ place 場所 東京駅の顔出しパネル、登場店舗、宿泊場所、観光名所、施設、交通拠点 [リソース]
    """

####op ['verbose_name="{verbose}"', 'auto_now_add=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'auto_now_add=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')


class Step(models.Model):
    """ step 訪問 [イベント]
    """

####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')


class Scene(models.Model):
    """ scene シーン 名シーン、ざつ旅ARのマーカー [イベント]
    """

####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')


class Character(models.Model):
    """ character キャラクター 主要5人、編集部、他 [リソース]
    """

####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')


class Photo(models.Model):
    """ photo flickr (google place photo api有料) [リソース]
    """

####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')


class Tweet(models.Model):
    """ tweet Twitter 石坂さん、鈴ヶ森さん、読者等、無関係 [リソース]
    """

####op ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['"{relation}"', 'verbose_name="{verbose}"', 'related_name="{relname}"', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE', 'on_delete=models.CASCADE'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')


class User(models.Model):
    """ user ユーザー 利用者 [リソース]
    """

####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'max_length=255', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'max_length=255', 'blank=True'], '    )')
####op ['verbose_name="{verbose}"', 'blank=True']
####tmpl ('    {mark}{name} {verbose} {description}{mark}', '    {name} = models.{model_type}(', ['verbose_name="{verbose}"', 'blank=True'], '    )')


class Group(models.Model):
    """ group グループ [リソース]
    """

