
jQuery("document").ready(function(){
    var count = 2;

    function alternative_button_visibility(id){
        if (count > 2){
            jQuery("#" + id).show();
        }else{
            jQuery("#" + id).hide();
        }
    }

    alternative_button_visibility("delete_alternative_button", count);
    alternative_button_visibility("delete_category_button", count);

    jQuery("#add_alternative_button").on("click", function(){
        count = count + 1;
        jQuery("#alternatives").append("<div id=\"div_alternative" + count
        + "\" class=\"container-fluid\"><p>Альтернатива " + count
        + ": <input required type=\"text\" name=\"alternative" + count
        + "\" class=\"form-control\"></p></div>");

        alternative_button_visibility("delete_alternative_button");
    });

    jQuery("#delete_alternative_button").on("click", function(){
        if (count > 2){
            jQuery("#div_alternative" + count).remove();
            count = count - 1;
            alternative_button_visibility("delete_alternative_button");
        }
    });

    jQuery("#add_category_button").on("click", function(){
        count = count + 1;
        var html_text = "<div id=\"div_category" + count + "\" class=\"container\"> \
                Категорія " + count + ": \
                <div class=\"row\"> \
                    <div class=\"col-md-8\"> \
                        <input required type=\"text\" name=\"category" + count + "\" class=\"form-control\"> \
                    </div> \
                    <div class=\"col-md-4\"> \
                        <select name=\"value" + count + "\" class=\"form-control\"> \
                            <option value=\"1\">1</option> \
                            <option value=\"2\">2</option> \
                            <option value=\"3\">3</option> \
                            <option value=\"4\">4</option> \
                            <option value=\"5\">5</option> \
                            <option value=\"5\">6</option> \
                            <option value=\"7\">7</option> \
                            <option value=\"8\">8</option> \
                            <option value=\"9\">9</option> \
                        </select> \
                    </div> \
                </div> \
            </div>";

        jQuery("#categories").append(html_text);

        alternative_button_visibility("delete_category_button");
    });

    jQuery("#delete_category_button").on("click", function(){
        if (count > 2){
            jQuery("#div_category" + count).remove();
            count = count - 1;
            alternative_button_visibility("delete_category_button");
        }
    });

})
