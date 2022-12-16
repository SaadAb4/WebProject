<template>
<div>
  <button @click="fetchItems" class="btn btn-warning">Search Items</button>
  <li v-for ="item in items" v-bind:key="item.id">
  <div class="card mb-3 bg-info text-white ">
    <img class="card-img-top" src="..." alt="image not available">
    <div class="card-body"><h3 class="card-title">{{item.title}}</h3>
      <div class="card-body">
      <p class="card-text">{{item.description}} </p>
      <p class="card-text"> <span class="badge badge-pill badge-success">Price: £{{item.startingPrice}}</span> </p>
      <p class="card-text"><small class="text-muted"> {{item.auctionEnd}} </small></p>
      <button class="btn btn-danger">Bid</button>
      </div>
    </div>
  </div>

  </li>
        
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
        let response = await fetch("http://localhost:8000/api/items/")
        let data = await response.json()
        this.items = data.items
      },
      }
    }
</script>