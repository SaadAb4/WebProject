<template>
    <div class="profileBody ">  
        <div class="pictureHolder p-3 mb-2 bg-dark"></div>
        <form>
        <div class="form-group">
            <label for="exampleFormControlFile1">Example file input</label>
            <input type="file" class="form-control-file" id="exampleFormControlFile1" v-on="item_pic">
        </div>
    
        <div class="form-group">
        <label for="itemName">ITEM NAME</label>
        <input type="text" class="form-control" id="itemName" placeholder="what is the item" v-model="title">
        <label for="itemDescrip">ITEM DESCRIPTION</label>
        <input type="text" class="form-control" id="itemDescrip"  placeholder="input description of the item here.." v-model="description">
        <label>starting price</label>
        <input type="decimal" class="form-control" placeholder="£" v-model="startingPrice">
        
        </div>
        
        <div>
        <input type="date" id="doe" min="1900-01-01" max="current" v-model="auctionEnd">
        </div> 
        <button type="submit" class="btn btn-primary" @click="additem"> Submit</button>

    </form>
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
        async additem()
            {
            let response = await fetch("http://localhost:8000/api/items/",{
                method : 'POST',
                header : {'Content-Type' : 'application/json',},
                  body: JSON.stringify({
                  title: this.title,
                  description: this.description,
                  startingPrice: this.startingPrice,
                  auctionEnd: this.auctionEnd,
                  item_pic: this.item_pic
                  })
              })
            }

        }
    }
        



</script>