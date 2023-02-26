
var backend_base_url = "http://localhost:5000/"

async function request_func(url) {
    var request = await fetch(url)
    var response = await request.json()
    return response
}

// function input_check() {
//     var fullname = document.getElementById("fullname")
//     var email = document.getElementById("email")
//     var gradyear = document.getElementById("gradyear")
//     var gender = document.getElementById("gender")
//     var school = document.getElementById("school")
//     var major = document.getElementById("major")
//     var attended = document.getElementById("attended")
//     var industry = document.getElementById("industry")
//     var interest = document.getElementById("interests")

//     if(!fullname.checkValidity())fullname.reportValidity()
//     else if(!email.checkValidity())email.reportValidity()
//     else if(!gradyear.checkValidity())gradyear.reportValidity()
//     else if(!gender.checkValidity())gender.reportValidity()
//     else if(!school.checkValidity())school.reportValidity()
//     else if(!major.checkValidity())major.reportValidity()
//     else if(!attended.checkValidity())attended.reportValidity()
//     else if(industry.checkValidity())industry.reportValidity()
//     else if(interest.checkValidity())interest.reportValidity()
//     else{
//         new_user_submit()
//     }

// }
async function after_login(){
    alert("INSIDE FUNCTION AFTER LOGIN")

    var email = document.getElementById("username").value
    var password = document.getElementById("password").value

    //request
    var backend_url = backend_base_url
    backend_url += "login_request?"
    backend_url += "email=" + email
    backend_url += "&password=" + password

    backend_login_response = await request_func(backend_url)
    // show the response to the client

    text = ""
    


}


async function new_user_submit(){
    var fullname = document.getElementById("fullname").value
    var email = document.getElementById("email").value
    var gradyear = document.getElementById("gradyear").value
    var gender = document.getElementById("gender").value
    var school = document.getElementById("school").value
    var major = document.getElementById("major").value
    var attended = document.getElementById("attended").value
    var industry = document.getElementById("industry").value
    var interest = document.getElementById("interests").value

    var beginner = document.getElementById("beginner").value
    var workshop = document.getElementById("workshop").value
    var speaker = document.getElementById("speaker").value
    var networking = document.getElementById("networking").value
    var overallexp = document.getElementById("overallexp").value


    var backend_url = backend_base_url
    console.log("industry:",industry)
    console.log("interest",interest)
    backend_url += "new_user_request?fullname="+ fullname + "&email=" + email + "&gradyear=" +gradyear+ "&gender=" + gender + "&school=" + school
    backend_url += "&major=" + major + "&attended=" + attended + "&industry=" + industry + "&interest=" + interest

    if(typeof beginner != null && beginner.length > 0){
        console.log("beginner",beginner)
        backend_url += "&beginner=" + beginner
    }

    if(typeof beginner != null && workshop.length > 0){
        backend_url += "&workshop=" + workshop
    }

    if(speaker.length > 0){
        backend_url += "&speaker=" + speaker
    }

    if(networking.length > 0){
        backend_url += "&networking=" + networking
    }

    if(overallexp.length > 0){
        backend_url += "&overallexp=" + overallexp
    }


    console.log("new user submit url:",backend_url)
    backend_url.replace(" ","%20")

    backend_new_user_response = await request_func(backend_url)
    console.log("response new:",backend_new_user_response)

    inner_text = ""
    for(let i = 0;i < backend_new_user_response.length; i++){
        inner_text += "<div class=similar_style><p>Get Connected With " + backend_new_user_response[i].fullname + "</p>"
        inner_text += "<p>Email:" + backend_new_user_response[i].email + "</p></div>"
 
    }

    document.getElementById("similar_person").innerHTML = inner_text
    console.log("result:",document.getElementById("similar_person").value)
    document.getElementById("input_form").hidden = true
}

async function after_comment(){
    var email = document.getElementById("email").value
    var comment= document.getElementById("comment").value

    email = email.replace("@","")
    email = email.replace(".","")

    var backed_url = backend_base_url+"comment_request?email=" + email
    backed_url += "&comment=" + comment

    backend_comment_response = await request_func(backend_url)

    // parse the data and show the resonse to the front end

}

async function after_star(){
    var email = document.getElementById("email").value
    var star= document.getElementById("star").value

    email = email.replace("@","")
    email = email.replace(".","")

    var backend_url = backend_base_url +"star_request?"
    backend_url += "email=" + email
    backend_url += "&star=" + star

    console.log("star url:",backend_url)

    backend_star_response = await request_func(backend_base_url)

    //parse the data and show the response to the front end
}