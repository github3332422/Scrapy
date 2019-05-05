#按照单页模式进行操作
#工作名字
name = response.xpath("//dd[@class='job_request']//span")

#工资,工作城市,经验,教育,工作性质
job_requests_spans = html.xpath("//dd[@class='job_request']//span")
salary = job_requests_spans[0].xpath('.//text()')[0].strip()
city = job_requests_spans[1].xpath('.//text()')[0].strip()
city = re.sub(r"[\s/]", "", city)
work_year = job_requests_spans[2].xpath('.//text()')[0].strip()
work_year = re.sub(r"[\s/]", "", work_year)
education = job_requests_spans[3].xpath('.//text()')[0].strip()
education = re.sub(r"[\s/]", "", education)
work_nature = job_requests_spans[4].xpath('.//text()')[0].strip()

#职位诱惑
job_detail = "".join(html.xpath("//dd[@class='job-advantage']//text()")).strip()
job_detail = job_detail.replace('\n', '')
job_detail = job_detail.replace(' ', '')

#公司名字
company = "".join(html.xpath("//h2[@class='fl']//text()"))
company = company.replace('\n', '')
company = company.replace(' ', '')[0:-6]

#发表时间
release_time = html.xpath("//p[@class='publish_time']//text()")

#职位要求
zhiwei = str(html.xpath("//div[@class='job-detail']//text()"))
zhiwei = zhiwei.replace('\\n', '')
zhiwei = zhiwei.replace(' ', '')
zhiwei = zhiwei.replace("'',", '')
zhiwei = str(zhiwei)
index = zhiwei.index("岗位要求：")
duties = zhiwei[0:index]
claim = zhiwei[index:-1]

#工作地点
place = response.xpath("//div[@class='work_addr']/a//text()")






