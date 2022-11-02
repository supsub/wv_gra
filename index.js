$(document).ready(function(){
    const url = "https://us-central1-third-harbor-367421.cloudfunctions.net/input_password_get_link"
    $('#btn').click(function(){
        var guess = document.getElementById('guess').value
        document.getElementById('result').innerHTML = "Loaaaaading...."
        $.ajax({
            url: `${url}?guess=${guess}`,
            type: "GET",
            success: function(result){
                console.log(result)
                if (result.slice(0,8) === 'https://'){
                    document.getElementById('result').innerHTML = `${result}  😘 😘 😘`
                }
                else {
                    document.getElementById('result').innerHTML = "Sory gregory  😞"
                }
            },
            error: function(result){
                console.log(`Error: ${result}`)
            }
        })
    })
})
