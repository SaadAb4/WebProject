<template>
    <div>
        <form class="" method="post">
            <div class="container">
            <label for="email"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" name="email" required>

            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>
                
            <button type="submit">Login</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
            </div>

            <div class="container" >
            <button type="button" onclick="document.getElementById('login').style.display='none'" class="cancelbtn">Cancel</button>
            </div>
        </form>

        <!-- signup -->

        <form class="" method="post">
            <div class="container">
            <label for="email"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" name="email" required>

            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>

            <label for="dob"><b>Date of Birth</b></label>
            <input type="date" placeholder="Enter Date of Birth" name="dob" required>
                
            <button type="submit">Sign Up</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
            </div>

            <div class="container" >
            <button type="button" onclick="document.getElementById('login').style.display='none'" class="cancelbtn">Cancel</button>
            </div>
        </form>
    </div>
</template>