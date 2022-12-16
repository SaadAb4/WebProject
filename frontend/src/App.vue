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
    <router-view/>
    </div>

  
  </div>
</template>
  
  
<script>
  export default {
    data() {
      return {
        name: "Mr Malik",
        counter: 0,
      }
    },
    methods: {
      async fetchItems() {
        let response = await fetch("http://localhost:8000/api/music/")
        let data = await response.json()
        this.items = data.items
      },


      }
    }
</script>
  

  
  

  