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
                var popup_json = document.getElementById('json');
                popup_json = response
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
