<template>
<!--    <nav class="navbar navbar-fixed-top navbar-inverse">-->
<!--      <div class="container">-->
<!--        <div class="navbar-header">-->
<!--          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">-->
<!--            <span class="sr-only">Toggle navigation</span>-->
<!--            <span class="icon-bar"></span>-->
<!--            <span class="icon-bar"></span>-->
<!--            <span class="icon-bar"></span>-->
<!--          </button>-->
<!--          <a class="navbar-brand" href="#">Project name</a>-->
<!--        </div>-->
<!--        <div id="navbar" class="collapse navbar-collapse">-->
<!--          <ul class="nav navbar-nav">-->
<!--            <li class="active"><a href="#">Home</a></li>-->
<!--            <li><a href="#about">About</a></li>-->
<!--            <li><a href="#contact">Contact</a></li>-->
<!--          </ul>-->
<!--        </div>-->
<!--      </div>-->
<!--    </nav>-->

  <div class="container">

      <div class="row row-offcanvas row-offcanvas-right">

        <div class="col-xs-12 col-sm-9">
          <p class="pull-right visible-xs">
            <button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle nav</button>
          </p>
          <div class="jumbotron">
            <h1>Hello, world!</h1>
            <p>This is an example to show the potential of an offcanvas layout pattern in Bootstrap. Try some responsive-range viewport sizes to see it in action.</p>
          </div>
          <div class="row">
            <div class="col-xs-6 col-lg-4" v-for="blog in bloglist">
              <h2>{{ blog.title }}</h2>
              <p>{{ blog.content }}</p>
              <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
            </div><!--/.col-xs-6.col-lg-4-->
          </div><!--/row-->
        </div><!--/.col-xs-12.col-sm-9-->

        <div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar">
          <div class="list-group">
            <a href="#" class="list-group-item active">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
            <a href="#" class="list-group-item">Link</a>
          </div>
        </div><!--/.sidebar-offcanvas-->
      </div><!--/row-->
<!--  <div class="container">-->
<!--    <div class="column" v-for="blog in bloglist">-->
<!--          <h2>-->
<!--            {{ blog.title }}-->
<!--          </h2>-->
<!--            <p>{{ blog.content }}.</p>-->
<!--    </div>-->
<!--&lt;!&ndash;      <button @click="getData">GET DATA</button>&ndash;&gt;-->
    <hr>

      <footer>
        <p>&copy; 2016 Company, Inc.</p>
      </footer>
  </div>
</template>

<script>

    import axios from 'axios';
    import 'bootstrap/dist/js/bootstrap.min.js'

    export default {
        name: "Archive",
        data: function() {
            return {
              bloglist: [],
              // list: []
            }
        },
        created(){
            var that = this;
            axios.get('http://127.0.0.1:5000/api/bloglist').then(function (response) {
                that.bloglist = response.data;
            }).catch(function (error) {
                alert('Error ' + error);
            })
        },
        methods: {
          getData() {
            var that = this;
            // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
            const path = 'http://127.0.0.1:5000/api/bloglist';
            axios.get(path).then(function (response) {
              // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
              // 可以直接通过 response.data 取key-value
              // 坑一：这里不能直接使用 this 指针，不然找不到对象
              // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
              that.list = response.data;
              // alert('Success ' + response.status + ', ' + response.data + ', ' + content);
                console.log(that.list)
            }).catch(function (error) {
              alert('Error ' + error);
            })
          }
        }
      }
</script>

<style scoped>
  /*@import '../assets/dist/css/bootstrap.min.css';*/
  /*@import '../assets/dist/css/bootstrap.css';*/
  /*@import '../assets/dist/css/offcanvas.css';*/
</style>
