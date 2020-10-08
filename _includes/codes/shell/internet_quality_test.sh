test_website_list='www.chiphell.com www.zhihu.com www.new.qq.com www.ithome.com'

for i in $test_website_list; do
    echo $i
    ping -c 5 -q $i |grep rtt
done
