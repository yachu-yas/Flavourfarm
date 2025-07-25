document.addEventListener("DOMContentLoaded", function() {
    var productBoxes = document.querySelectorAll(".productBox");

    productBoxes.forEach(function(productBox) {
        var plusBtn = productBox.querySelector(".plus");
        var minusBtn = productBox.querySelector(".minus");
        var qtyInput = productBox.querySelector("input[type='number']");
        var stock = parseInt(productBox.getAttribute("data-stock"), 10);

        // Set the initial quantity to 1
        qtyInput.value = 1;

        plusBtn.addEventListener("click", function() {
            if (qtyInput.value < stock) {
                qtyInput.value = parseInt(qtyInput.value) + 1;
            }
        });

        minusBtn.addEventListener("click", function() {
            if (qtyInput.value > 1) {
                qtyInput.value = parseInt(qtyInput.value) - 1;
            }
        });
    });
});
