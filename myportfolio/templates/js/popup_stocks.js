<div>
<input type="hidden" id="ajax-url" value="{% url 'text2stocks' %}"></input>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<script>
    var submitBtn = document.getElementById('process_btn');
    var headline = document.getElementById('headline');
    // headline.value = "Test"
                    
    // Add click event listener
    submitBtn.addEventListener('click', function() {
        // Collect Paramters
        var blog_id = $('#blog_id').val();
        var ref_stocks = $('#id_referencedStocks').val();
        var headline = $('#headline').val();
        var url = $('#ajax-url').val();

        $.ajax({
            url: url,
            type: 'GET',
            data: {
                'blog_id': blog_id,
                'ref_stocks': ref_stocks,
                'headline': headline,
            },
            success: function(response) {
                // Handle successful response
                var popupForm = document.getElementById('popup-form');
                popupForm.style.display = 'block';
                var popup_blog_id = document.getElementById('popup_blog_id');
                popup_blog_id.value = response.blog_id + ": " + response.headline
                var popup_stocks = document.getElementById('popup_ref_stocks');
                popup_stocks.value = response.ref_stocks
                var popup_stock_table = document.getElementById('popup_stock_table');
                var headerRow = document.createElement('tr');
                var headers = ['Stock', 'WKN','ISIN', 'SYMBOL', 'New'];
                headers.forEach(function(headerText) {
                    var headerCell = document.createElement('th');
                    headerCell.textContent = headerText;
                    headerRow.appendChild(headerCell);
                });
                popup_stock_table.appendChild(headerRow);

                for (var i = 0; i < response.shares.length; i++) {
                    var item = response.shares[i];
                    var row = popup_stock_table.insertRow();
                    if (item.conflict){
                        row.style.backgroundColor = 'red';
                        var button = document.getElementById('submitButton');
                        button.disabled = true;
                    }
                    var cell1 = row.insertCell(0);
                    cell1.innerHTML = item.name;
                    var cell2 = row.insertCell(1);
                    cell2.innerHTML = item.wkn
                    var cell3 = row.insertCell(2);
                    cell3.innerHTML = item.isin
                    var cell4 = row.insertCell(3);
                    cell4.innerHTML = item.symbol
                    var cell5 = row.insertCell(4);

                    var cell5 = row.insertCell(4);
                    var checkbox = document.createElement('input');
                    checkbox.type = 'checkbox';
                    checkbox.disabled = true;
                    checkbox.checked = item.new;
                    cell5.appendChild(checkbox);
                }
            },
            error: function(xhr, status, error) {
                // Handle error
                console.error(error);
            }
        });
    });

    function closePopup() {
        document.getElementById('popup-form').style.display = 'none';
    };

    function saveStocks() {
        headline.value = "Save";
        document.getElementById('popup-form').style.display = 'none';
    }

</script>
</div>
