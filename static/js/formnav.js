
	document.getElementById('').onclick = function() {myFunction()};
			
	
	function myFunction() {
	document.getElementById('').classList.toggle('show');
	};

<script>
function validateForm() {
  var x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Name must be filled out");
  }
}
</script>

------------------------------------------navbar scroll
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}
-----------------------------------------navbar scroll size change
function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("navbar").style.padding = "30px 10px";
  
  } else {
    document.getElementById("navbar").style.padding = "80px 10px";
  }
};
innerHTML
getElementsByClassName



    <!--    nav click content-- >
                    function mDown_feedback() {

        document.getElementById('fd').classList.toggle('show');

                    };

                function myFunction_feedback() {
        document.getElementById("mystyle").classList.toggle("mystyle");
                };

                function mDown_contact() {

        document.getElementById('fd2').classList.toggle('show');

                };

                function myFunction_contact() {
        document.getElementById("mystyle2").classList.toggle("mystyle2");
                };
