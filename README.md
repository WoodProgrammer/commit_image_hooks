# GitHooks Docker Builder 
 
## TÜRKÇE

Git Server'ı uzaktaki makinede kurmak için uzaktaki makinede aşağıdaki komutları çalıştırın.
```sh
   $ git_server_scripts/stup.sh
```
### GitHooks 
Githooks bizler için CI süreçlerini hızlandırmamızı ve otomatize etmemizi sağlayan bir yapıdır.
Githook içerisinde sahip olduğu eventler sayesinde yapılması gereken işleri tetikler.

Bu eventlere örnek verecek olursak.
* post_recevie 
- pre_receive
* pre_commit 

gibi onlarca event githooks tarafından bilinmektedir.

* post_receive: 

```sh
Bulunulan repoya herhangi bir push geldiğinde buraya subscribe
edilmiş işlemler yaptırılır.

```

* pre_commit :

```sh
Siz Commit atmadan önce developer tarafta çalıştırılan 
eventleri ekliyoruz.Mesela testlerimizi yazdık ve pre_commit 
eventlerimize testlerimizi çalıştırabilmesini sağlayabiliriz.

```
Ben şuanlık projemizde kullanacağımız eventleri açıkladım.

###Bu projemizde nerede kullandık?

* Pre_Receive eventi bizim gelen pushları alıp docker imagelarını 
build ediyor ve kendi registrymize gönderiyor veya dockerhubda sizin kendi hesabınıza
son imageı göndermektedir.

###Kurulum
```sh

    Devamı gelecek .
```



# ENG
For setup git server on your remote machine run this on your remote machine.

Githooks is structure make our CI process fast.Githooks trigger the which process subscribe on it.

Githooks triggering though of its own events it has.

For example 
* post_recevie 
- pre_receive
* pre_commit 

we  have lots of githooks events.

Explanation some events :

* post_receive: 

This event to do jobs if repository got new push.
* pre_commit :


Pre Commit is usign on developer side.You can write your tests
and work before commiting process.Commiting process trigger the 
pre-commit event.

I explained the events above which events to use in this project

Where used in this Project ?

* If any commit pushed on your local git repository,post_receive
event build the docker image and push where you want(DockerHub or your own DockerRegistry).


###Kurulum
```sh
       Coming soon .
```
  

