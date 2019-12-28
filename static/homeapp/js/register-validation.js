function regval()
{ 
    var name = document.forms["RegPage"]["FullName"];
    var email = document.forms["RegPage"]["Email"];
    var mobile = document.forms["RegPage"]["Mobile"];
    var password1 = document.forms["RegPage"]["Password1"];
    var password2 = document.forms["RegPage"]["Password2"];

   
    if (name.value == "")                                  
    { 
        window.alert("Please enter your name."); 
        name.focus(); 
        return false; 
    } 

    if (email.value == "")                                   
    { 
        window.alert("Please enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
   
    if (mobile.value == "")
    { 
        window.alert("Please enter your mobile number.");
        phone.focus(); 
        return false; 
    } 
   // If password not entered
    if (password1.value == '')
        alert ("Please enter Password");

    // If confirm password not entered
    else if (password2.value == '')
     alert ("Please enter confirm password");

    // If Not same return False.
    else if (password1.value != password2.value)
    {
        alert ("\nPassword did not match: Please try again...")
        return false;
    }

    // If same return True.
    else
    {
        alert("Password Match: Welcome!")
        return true;
    }
    return true;

}