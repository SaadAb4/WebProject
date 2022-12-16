<template>
    <div class="profileBody ">  
        <div class="pictureHolder p-3 mb-2 bg-dark"></div>
        <form>
        <div class="form-group">
            <label for="exampleFormControlFile1">Example file input</label>
            <input type="file" class="form-control-file" id="exampleFormControlFile1">
        </div>
    
        <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
        </div>
        
        <div>
        <input type="date" id="dob"
        value=""
        min="1900-01-01" max="current">
        </div> 
        <button type="submit" class="btn btn-primary">Submit</button>

    </form>
  </div>
</template>