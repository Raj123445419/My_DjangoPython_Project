document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");

    const searchResults = document.getElementById("searchResults");


    searchInput.addEventListener("keyup", function () {

        let query = searchInput.value;


        // REMOVE OLD RESULTS
        if (query.length === 0) {

            searchResults.innerHTML = "";

            return;
        }


        fetch(`/search/?q=${query}`)

            .then(response => response.json())

            .then(data => {

                searchResults.innerHTML = "";


                // NO PRODUCT FOUND
                if (data.products.length === 0) {

                    searchResults.innerHTML = `

                        <div class="no-result">
                            No product found
                        </div>

                    `;

                    return;
                }


                // SHOW PRODUCTS
                data.products.forEach(product => {

                    searchResults.innerHTML += `

                        <a href="/${product.page}"
                           class="search-item">

                            <img src="${product.image}">

                            <span>${product.name}</span>

                        </a>

                    `;
                });

            });

    });

});