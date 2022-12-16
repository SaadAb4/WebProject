<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light ">
    <a class="navbar-brand" href="#">Welcome {{name}} </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link class="nav-link" to="/"> Home </router-link>
        </li>
        <li class="nav-item active">
          <router-link class="nav-link" to="/profile"> Profile </router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/login"> LogIn </router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/loginpage">Login html</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">post new item</a>
        </li>
      </ul>
      </div>
      <form class="forms">
      <input class="form-control mr-sm-2" type="search" placeholder="Search for an item" aria-label="Search">
      <button class="btn btn-outline-success btn-inline my-2 my-sm-0" type="submit">Search</button>
    </form>
    </nav>
    
    <div class="routed">
      <div class="p-3 mb-2 bg-secondary text-white">
        <button @click="fetchItems" class="btn btn-info">Fetch Items</button>
        <div>{{items}}</div>
        <form>
          <div>
            <label for="title" class="p-3 mb-2 bg-dark text-white">Restaurant Name</label>
            <input type="text" id="title" v-model="title"/>
          
          
            <label for="rating" class="p-3 mb-2 bg-dark text-white">Rate the Restaurant</label>
            <input type="number" id="rating" v-model="description"/>
          </div>
          <div>
            <label for="date" class="p-3 mb-2 bg-dark text-white">Date of last visit</label>
            <input type="date" id="date" v-model="startingPrice"/>
          
          
            <label for="email" class="p-3 mb-2 bg-dark text-white">Your email</label>
            <input type="email" id="email" v-model="auctionEnd"/>
            <label for="pic" class="p-3 mb-2 bg-dark text-white">Your email</label>
            <input type="email" id="email" v-model="auctionEnd"/>
          </div>
        </form>
        <button @click="postRestaurants" class="btn btn-info">Add rating</button>
      
    </div>`
    <router-view/>
    </div>

  
  </div>
</template>
  
  
<script>
  export default {
    data() {
      return {
        items:[],
        title:'',
        description:'',
        startingPrice:'',
        auctionEnd:'',
        item_pic:'',
      }
    },
    methods: {
      async fetchItems() {
        let response = await fetch("http://127.0.0.1:8000/coursework3/items/")
        let data = await response.json()
        this.items = data.items
      },
      }
    }
</script>
  

  
  

  