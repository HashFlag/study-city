<template>
  <div class="course">
    <Header></Header>
    <div class="main">
      <!-- 筛选条件 -->
      <div class="condition">
        <ul class="cate-list">
          <li class="title">课程分类:</li>
          <li :class="category===0?'this':''" @click="category=0">全部</li>
          <li :class="category===item.id?'this':''" v-for="item in category_list" @click="category=item.id">
            {{item.name}}
          </li>
        </ul>
        <div class="ordering">
          <ul>
            <li class="title">筛&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;选:</li>
            <li class="default" :class="orders==='id'?'this asc':(orders==='-id'?'this desc':'')"
                @click="select_course_ordering('id')">默认
            </li>
            <li class="hot" :class="orders==='students'?'this asc':(orders==='-students'?'this desc':'')"
                @click="select_course_ordering('students')">人气
            </li>
            <li class="price" :class="orders==='price'?'this asc':(orders==='-price'?'this desc':'')"
                @click="select_course_ordering('price')">价格
            </li>
          </ul>
          <p class="condition-result">共21个课程</p>
        </div>

      </div>
      <!-- 课程列表 -->
      <div class="course-list">
        <div class="course-item" v-for="course in course_list">
          <div class="course-image">
            <img :src="course.course_img" :alt="course.name">
          </div>
          <div class="course-info">
            <h3 style="text-align: center;">
              <router-link :to="`/course/${course.id}`">{{course.name}}</router-link>
              <span><img src="/static/image/avatar1.svg" alt="">{{course.students}}人已加入学习</span></h3>
            <p class="teather-info" style="text-align: center;">{{course.teacher.name}} {{course.teacher.signature}} {{course.teacher.title}} <span>共{{course.lessons}}课时/{{course.lessons===course.pub_lessons?'已更新完成':`已更新${course.pub_lessons}课时`}}</span>
            </p>
            <ul class="lesson-list">
              <li v-for="(lesson,key) in course.recomment_lesson_list">
                <p class="lesson-title">0{{key+1}} | 第{{lesson.number}}节：{{lesson.name}}</p>
                <span class="free" v-if="lesson.free_trail">免费</span>
              </li>
            </ul>
            <div class="pay-box" v-if="course.discount_name">
              <span class="discount-type">{{course.discount_name}}</span>
              <span class="discount-price">￥{{course.discount_price}}元</span>
              <span class="original-price" v-if="course.discount_price!=course.min_price">原价：{{course.min_price}}元</span>
              <span class="buy-now">立即购买</span>
            </div>
            <div class="pay-box" v-else>
              <span class="discount-price">￥ {{course.min_price}}元</span>
              <span class="buy-now">立即购买</span>
            </div>
          </div>
        </div>
        <el-pagination background :page-size="size" :page-sizes="[2,5,10,20]"
                       layout="sizes, prev, pager, next" @size-change="handleSizeChange"
                       :current-page="page" @current-change="handleCurrentChange"
                       :hide-on-single-page="false" :total="course_total"></el-pagination>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
    import Header from "../common/Header";
    import Footer from "../common/Footer";

    export default {
        name: "Course",
        data() {
            return {
                category: 0,        // 当前用户勾选展示的课程分类
                category_list: [],  // 课程分类列表
                course_list: [],    // 课程列表
                orders: "id",      // 课程排序字段说明
                course_total: 0,   // 课程总数
                page: 1,           // 当前页页码
                size: 5,           // 每一页显示的数据量
            }
        },
        created() {
            this.get_category_list();
            this.get_course_list();
        },
        watch: {
            // 监听
            category() {
                this.page = 1;
                this.get_course_list();
            },
            orders() {
                this.page = 1;
                this.get_course_list();
            }
        },
        methods: {
            get_category_list() {
                // 获取课程分类列表
                this.$axios.get(`/courses/category/`).then(response => {
                    this.category_list = response.data;
                }).catch(error => {
                    console.log(error.response.data);
                })
            },
            get_course_list() {
                let params = {};
                if (this.category > 0) {
                    params = {
                        course_category: this.category,
                    }
                }
                params.ordering = this.orders;
                params.page = this.page;
                params.size = this.size;
                // 获取课程列表
                this.$axios.get(`/courses/`, {params}).then(response => {
                    this.course_list = response.data.results;
                    this.course_total = response.data.count;
                }).catch(error => {
                    console.log(error.response.data);
                })
            },
            select_course_ordering(order_field) {
                // 手动选择课程排序的字段
                if ((order_field === this.orders) && (this.orders[0] !== '-')) {
                    this.orders = "-" + this.orders;
                } else {
                    this.orders = order_field;
                }
            },
            handleSizeChange(size) {
                // 单页数据发生改变时触发的事件方法
                this.size = size;
                this.page = 1;
                this.get_course_list();
            },
            handleCurrentChange(page) {
                // 修改页码时，触发的事件方法
                this.page = page;
                this.get_course_list();
            }
        },
        components: {
            Header,
            Footer,
        }
    }
</script>

<style scoped>
  .course {
    background: #f6f6f6;
  }

  .course .main {
    width: 1100px;
    margin: 35px auto 0;
  }

  .course .condition {
    margin-bottom: 35px;
    padding: 25px 30px 25px 20px;
    background: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 4px 0 #f0f0f0;
  }

  .course .cate-list {
    border-bottom: 1px solid #333;
    border-bottom-color: rgba(51, 51, 51, .05);
    padding-bottom: 18px;
    margin-bottom: 17px;
  }

  .course .cate-list::after {
    content: "";
    display: block;
    clear: both;
  }

  .course .cate-list li {
    float: left;
    font-size: 16px;
    padding: 6px 15px;
    line-height: 16px;
    margin-left: 14px;
    position: relative;
    transition: all .3s ease;
    cursor: pointer;
    color: #4a4a4a;
    border: 1px solid transparent; /* transparent 透明 */
  }

  .course .cate-list .title {
    color: #888;
    margin-left: 0;
    letter-spacing: .36px;
    padding: 0;
    line-height: 28px;
  }

  .course .cate-list .this {
    color: #ffc210;
    border: 1px solid #ffc210 !important;
    border-radius: 30px;
  }

  .course .ordering::after {
    content: "";
    display: block;
    clear: both;
  }

  .course .ordering ul {
    float: left;
  }

  .course .ordering ul::after {
    content: "";
    display: block;
    clear: both;
  }

  .course .ordering .condition-result {
    float: right;
    font-size: 14px;
    color: #9b9b9b;
    line-height: 28px;
  }

  .course .ordering ul li {
    float: left;
    padding: 6px 15px;
    line-height: 16px;
    margin-left: 14px;
    position: relative;
    transition: all .3s ease;
    cursor: pointer;
    color: #4a4a4a;
  }

  .course .ordering .title {
    font-size: 16px;
    color: #888;
    letter-spacing: .36px;
    margin-left: 0;
    padding: 0;
    line-height: 28px;
  }

  .course .ordering .this {
    color: #ffc210;
  }

  .course .ordering .price {
    position: relative;
  }

  .course .ordering .this::before,
  .course .ordering .this::after {
    cursor: pointer;
    content: "";
    display: block;
    width: 0px;
    height: 0px;
    border: 5px solid transparent;
    position: absolute;
    right: 0;
  }

  .course .ordering .this::before {
    border-bottom: 5px solid #ffc210;
    margin-bottom: 2px;
    top: 2px;
  }

  .course .ordering .this::after {
    border-top: 5px solid #ffc210;
    bottom: 2px;
  }

  .course .ordering .asc::after {
    border-top: 5px solid #aaa;
    bottom: 2px;
  }

  .course .ordering .desc::before {
    border-bottom: 5px solid #aaa;
    bottom: 2px;
  }

  .course .course-item:hover {
    box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
  }

  .course .course-item {
    width: 1050px;
    background: #fff;
    padding: 20px 30px 20px 20px;
    margin-bottom: 35px;
    border-radius: 2px;
    cursor: pointer;
    box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
    /* css3.0 过渡动画 hover 事件操作 */
    transition: all .2s ease;
  }

  .course .course-item::after {
    content: "";
    display: block;
    clear: both;
  }

  /* 顶级元素 父级元素  当前元素{} */
  .course .course-item .course-image {
    float: left;
    width: 423px;
    height: 210px;
    margin-right: 30px;
  }

  .course .course-item .course-image img {
    width: 100%;
  }

  .course .course-item .course-info {
    float: left;
    width: 596px;
  }

  .course-item .course-info h3 {
    font-size: 26px;
    color: #333;
    font-weight: normal;
    margin-bottom: 8px;
  }

  .course-item .course-info h3 span {
    font-size: 14px;
    color: #9b9b9b;
    float: right;
    margin-top: 14px;
  }

  .course-item .course-info h3 span img {
    width: 11px;
    height: auto;
    margin-right: 7px;
  }

  .course-item .course-info .teather-info {
    font-size: 14px;
    color: #9b9b9b;
    margin-bottom: 14px;
    padding-bottom: 14px;
    border-bottom: 1px solid #333;
    border-bottom-color: rgba(51, 51, 51, .05);
  }

  .course-item .course-info .teather-info span {
    float: right;
  }

  .course-item .lesson-list::after {
    content: "";
    display: block;
    clear: both;
  }

  .course-item .lesson-list li {
    float: left;
    width: 44%;
    font-size: 14px;
    color: #666;
    padding-left: 22px;
    /* background: url("路径") 是否平铺 x轴位置 y轴位置 */
    background: url("/static/image/play-icon-gray.svg") no-repeat left 4px;
    margin-bottom: 15px;
  }

  .course-item .lesson-list li .lesson-title {
    /* 以下3句，文本内容过多，会自动隐藏，并显示省略符号 */
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
    display: inline-block;
    max-width: 200px;
  }

  .course-item .lesson-list li:hover {
    background-image: url("/static/image/play-icon-yellow.svg");
    color: #ffc210;
  }

  .course-item .lesson-list li .free {
    width: 34px;
    height: 20px;
    color: #fd7b4d;
    vertical-align: super;
    margin-left: 10px;
    border: 1px solid #fd7b4d;
    border-radius: 2px;
    text-align: center;
    font-size: 13px;
    white-space: nowrap;
  }

  .course-item .lesson-list li:hover .free {
    color: #ffc210;
    border-color: #ffc210;
  }

  .course-item .pay-box::after {
    content: "";
    display: block;
    clear: both;
  }

  .course-item .pay-box .discount-type {
    padding: 6px 10px;
    font-size: 16px;
    color: #fff;
    text-align: center;
    margin-right: 8px;
    background: #fa6240;
    border: 1px solid #fa6240;
    border-radius: 10px 0 10px 0;
    float: left;
  }

  .course-item .pay-box .discount-price {
    font-size: 24px;
    color: #fa6240;
    float: left;
  }

  .course-item .pay-box .original-price {
    text-decoration: line-through;
    font-size: 14px;
    color: #9b9b9b;
    margin-left: 10px;
    float: left;
    margin-top: 10px;
  }

  .course-item .pay-box .buy-now {
    width: 120px;
    height: 38px;
    background: transparent;
    color: #fa6240;
    font-size: 16px;
    border: 1px solid #fd7b4d;
    border-radius: 3px;
    transition: all .2s ease-in-out;
    float: right;
    text-align: center;
    line-height: 38px;
  }

  .course-item .pay-box .buy-now:hover {
    color: #fff;
    background: #ffc210;
    border: 1px solid #ffc210;
  }
</style>


