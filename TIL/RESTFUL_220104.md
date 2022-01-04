# Restful API
***
>HTTP 통신에서 어떤 자원에 대한 CRUD 요청을 Resource와 Method로 표현하여 특정한 형태로 전달하는 방식

즉 간단하게 말해</br>
어떤 자원에 CRUD(Create, Read, Update, Delete) 연산을 수행하기 위해 URI(Resource)로 요청을 보내는 것으로,</br>
Get, Post, Delete, Put, Patch 등의 방식(Method)을 사용하여 요청을 보내며,</br>
요청을 위한 자원은 특정한 형태(Representation of Resource)으로 표현된다.</br>

>RestFul 구성요소
> - Resource:</br>
> 서버는 Unique한 ID를 가지는 Resource를 가지고 있으며,</br>
>  클라이언트는 이러한 Resource에 요청을 보내고, 이러한 Resource는 URI에 해당
> 
> - Method:</br>
> 서버에 요청하는 방식
> </br>
> - Representation of Resource</br>
> 클라이언트와 서버가 데이터를 주고받는 방식, 요즘은 주로 Json을 사용한다고 한다.

# RestAPI 규칙.
- URI는 명사를 사용한다.
- 슬래시로 계층 관계를 표현한다.
- URI의 마지막에는 슬래시를 붙이지 않는다.
- URI는 소문자로만 구성한다.
- 가독성이 떨어지는 경우 하이픈을 사용한다.
