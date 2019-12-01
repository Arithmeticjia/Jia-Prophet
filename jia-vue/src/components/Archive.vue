<template>
  <div>
    <div class="column" v-for="blog in list">
          <h2>
            {{ blog.title }}
          </h2>
            <p>{{ blog.content }}.</p>
    </div>
      <button @click="getData">GET DATA</button>
  </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Archive",
        data: function() {
            return {
              list: []
            }
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
  /* 创建三个相等的列 */
.column {
  float: left;
  width: 33.33%;
}
</style>
