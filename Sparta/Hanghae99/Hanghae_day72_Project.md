# [항해99 6기] 실전 프로젝트 (19) - 2022.05.18

<!-- TOC -->

- [[항해99 6기] 실전 프로젝트 19 - 2022.05.18](#%ED%95%AD%ED%95%B499-6%EA%B8%B0-%EC%8B%A4%EC%A0%84-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-19---20220518)
- [Retrospect](#retrospect)

<!-- /TOC -->

# Retrospect
예전에 ngin로 리버스프록시를 설정할때는 금방했던거 같은데 이번에 적용시에는 며칠을 붙잡고 있었다.  
필요할때마다 그때그때 인터넷에서 찾아가면서 하는 나쁜 버릇을 고치기록 했으니 정리를 해 놓아야겠다.  
인터넷에 보면 ~~일해라 절해라~~ 말이 많은데 진행한 순서대로 기록해 놓자.

``` bash
$ sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
$ sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

$ sudo apt-get update -y

$ sudo add-apt-repository universe
$ sudo add-apt-repository ppa:certbot/certbot

$ sudo apt install certbot python3-certbot-nginx
$ sudo apt install nginx

$ sudo vim /etc/nginx/nginx.conf
# 아래 server의 내용 추가
...
        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;

        server {
                server_name yogoloper.shop;

                location / {
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        proxy_set_header Host $http_host;
                        proxy_set_header X-NginX-Proxy true;
                        proxy_pass http://127.0.0.1:3000/;
                        proxy_redirect off;
                }
        }
...

$ sudo systemctl enable nginx
$ sudo systemctl restart nginx

$ sudo certbot --nginx
$ sudo certbot renew --dry-run
```