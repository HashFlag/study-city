<template>
  <div class="header-box">
      <div class="header">
        <div class="content">
          <div class="logo full-left">
            <router-link to="/"><img src="/static/image/logo.svg" alt=""></router-link>
          </div>
          <ul class="nav full-left">
              <li :key="key" v-for="(nav,key) in nav_list">
                <a :href="nav.link" target="_blank" v-if="nav.is_http"><span>{{nav.name}}</span></a>
                <router-link :to="nav.link" v-else><span>{{nav.name}}</span></router-link>
              </li>
          </ul>
          <div v-if="token" class="login-bar full-right">
            <div class="shop-cart full-left">
              <img src="/static/image/cart.svg" alt="">
              <span><router-link to="/cart">购物车</router-link></span>
            </div>
            <div class="login-box login-box1 full-left">
              <router-link to="" class="study-ceneter">学习中心</router-link>
              <el-menu width="200" class="member el-menu-demo" mode="horizontal">
                  <el-submenu index="2">
                    <template slot="title"><router-link to=""><img src="/static/image/member.png" alt=""></router-link></template>
                    <el-menu-item index="2-1">我的账户</el-menu-item>
                    <el-menu-item index="2-2"><router-link to="/my/order">我的订单</router-link></el-menu-item>
                    <el-menu-item index="2-3">我的优惠卷</el-menu-item>
                    <el-menu-item index="2-3"><span @click="logoutHandle">退出登录</span></el-menu-item>
                  </el-submenu>
                </el-menu>
            </div>
          </div>
          <div v-show="!token" class="login-bar full-right">
            <div class="shop-cart full-left">
              <img src="/static/image/cart.svg" alt="">
              <span><router-link to="/cart">购物车</router-link></span>
            </div>
            <div class="login-box login-box2 full-left">
              <router-link to="/login"><span>登录</span></router-link>
              &nbsp;|&nbsp;
              <span class="header-register"><router-link to="/register">注册</router-link></span>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
      name: "Header",
      data(){
        return{
          token: true,
          nav_list:[],
          image:this.$settings.Host+localStorage.getItem("user_avatar"),
        }
      },
      created(){
          this.token = this.$settings.checkoutUserLogin(this);
          this.get_nav();
      },
      methods:{
          get_nav(){
              this.$axios.get(`/nav/header/`).then(response=>{
                  this.nav_list = response.data;
              })
          },
          logoutHandle(){
              // 退出登录处理
              localStorage.removeItem("token");
              sessionStorage.removeItem("token");
              // 记录用户积分
              sessionStorage.removeItem("user_credit");
              sessionStorage.removeItem("credit_rmb");
              this.token = "";
          }

      }
    }
</script>

<style scoped>
.header-box{
  height: 80px;
}
.header{
  width: 100%;
  height: 80px;
  box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  position: fixed;
  top:0;
  left: 0;
  right:0;
  margin: auto;
  z-index: 99;
  background: #fff;
}
.header .content{
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}
.header .content .logo{
  height: 80px;
  line-height: 80px;
  margin-right: 50px;
  cursor: pointer; /* 设置光标的形状为爪子 */
}
.header .content .logo img{
  vertical-align: middle;
}
.header .nav li{
  float: left;
  height: 80px;
  line-height: 80px;
  margin-right: 30px;
  font-size: 16px;
  color: #4a4a4a;
  cursor: pointer;
}
.header .nav li span{
  padding-bottom: 16px;
  padding-left: 5px;
  padding-right: 5px;
}
.header .nav li span a{
  display: inline-block;
}
.header .nav li .this{
  color: #4a4a4a;
  border-bottom: 4px solid #ffc210;
}
.header .nav li:hover span{
  color: #000;
}
.header .login-bar{
  height: 80px;
}
.header .login-bar .shop-cart{
  margin-right: 20px;
  border-radius: 17px;
  background: #f7f7f7;
  cursor: pointer;
  font-size: 14px;
  height: 28px;
  width: 88px;
  margin-top: 30px;
  line-height: 32px;
  text-align: center;
}
.header .login-bar .shop-cart:hover{
  background: #f0f0f0;
}
.header .login-bar .shop-cart img{
  width: 15px;
  margin-right: 4px;
  margin-left: 6px;
}
.header .login-bar .shop-cart span{
  margin-right: 6px;
}
.header .login-bar .login-box1{
  margin-top: 25px;
}
.header .login-bar .login-box2{
  margin-top: 32px;
}
.header .login-bar .login-box span{
  color: #4a4a4a;
  cursor: pointer;
}
.header .login-bar .login-box span:hover{
  color: #000000;
}
.member{
    display: inline-block;
    height: 34px;
    margin-left: 20px;
}
.member img{
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: inline-block;
}
.member img:hover{
  border: 1px solid yellow;
}
.el-menu.el-menu--horizontal{
  border-bottom: none;
}
.study-ceneter{
  display: inline-block;
  height: 34px;
  line-height: 34px;
  vertical-align: text-bottom;
}
</style>
