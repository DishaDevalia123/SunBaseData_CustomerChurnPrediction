function predictChurn() {
    var location = document.getElementById("location").value;
    var age = parseInt(document.getElementById("age").value);
    var subscriptionLength = parseInt(document.getElementById("sub-length").value);
    var monthlyBill = parseFloat(document.getElementById("monthly-bill").value);
    var totalUsage = parseFloat(document.getElementById("total-usage").value);
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/predict_churn", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  
    xhr.onload = function () {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        displayPredictionResult(response.prediction);
      } else {
        displayPredictionResult("Prediction failed. Please try again.");
      }
    };
  
    var data = JSON.stringify({
      location: location,
      age: age,
      subscriptionLength: subscriptionLength,
      monthlyBill: monthlyBill,
      totalUsage: totalUsage,
    });
  
    xhr.send(data);
  }
  
  function displayPredictionResult(result) {
    var resultField = document.getElementById("predicted-result");
    resultField.value = result;
  }
  
  
