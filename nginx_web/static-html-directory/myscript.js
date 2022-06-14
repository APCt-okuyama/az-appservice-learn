console.log("myscript start...")

//https://my-pythonapi-container-app.azurewebsites.net
API_URL = "https://my-pythonapi-container-app.azurewebsites.net"

axios.get(API_URL)
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });


console.log("myscript end")