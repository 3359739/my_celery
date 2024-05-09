from celery import Task
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


class timedata_cerely(Task):
    def on_success(self, retval, task_id, args, kwargs):
        # 任务成功后的回调函数
        info = f"任务成功,id:{task_id},参数:{args}结果:{retval}"
        send_mail("任务完成", info, settings.EMAIL_HOST_USER, ['3113217659@qq.com'])
        print("任务成功")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        # 任务失败后的回调函数
        info = f"任务失败,id:{task_id},参数:{args}结果:{exc}"
        send_mail("任务失败", info, settings.EMAIL_HOST_USER, ['3113217659@qq.com'])
        print("任务失败")


@shared_task(base=timedata_cerely, bind=True)
def baidu(name_args):
    print("爬取百度")
    print("爬取百度完成")
    return "百度"


from .models import bokeyou

from redis import  Redis
@shared_task(base=timedata_cerely, bind=True)
def crwaler_bokeyou(s):
    import requests
    from lxml import etree
    conn = Redis(host='127.0.0.1', port=6379)

    substance = requests.get('https://www.cnblogs.com/').text
    html = etree.HTML(substance)
    div = html.xpath('//div[@id="post_list"]/article')
    for i in div:
        txt = i.xpath('.//a/text()')[0].strip()
        url = i.xpath('.//a[@class="post-item-title"]/@href')[0].strip()
        author = i.xpath('.//a[@class="post-item-author"]//text()')[0]
        res = conn.sadd('urls', url)
        if res:
            print(conn.sadd('urls', url))
            bokeyou.objects.create(substance=txt, url=url, author=author)
            print(txt, url, author)

    return "爬取博客园完成"
