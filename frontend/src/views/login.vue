<template>
    <div>
        <form class="" method="post">
            <div class="container">
            <label for="email"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" name="email" required>

            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="password" required>
                
            <button type="submit" class="cancelbtn">Login</button>
            </div>
        </form>

        <!-- signup -->

        <form submit="post">
            <div class="container">
            <label for="email"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" name="email" required>

            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="password" required>

            <label for="dob"><b>Date of Birth</b></label>
            <input type="date" placeholder="Enter Date of Birth" name="dob" required>
                
            <button type="submit" class="cancelbtn">Sign Up</button>
            </div>

        </form>
    </div>
</template>
