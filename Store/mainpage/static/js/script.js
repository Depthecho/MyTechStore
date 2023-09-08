<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function () {
        $("#id_password1").on("focus", function () {
            $("#password-hint").css("display", "block");
        });

        $("#id_password1").on("blur", function () {
            $("#password-hint").css("display", "none");
        });
    });
</script>