document.addEventListener("DOMContentLoaded", function () {
	// dropdown initialization
	let dropdown = document.querySelectorAll(".dropdown-trigger");
	M.Dropdown.init(dropdown, {
		coverTrigger: false,
		hover: true,
	});
	// sidenav initialization
	let sidenav = document.querySelectorAll(".sidenav");
	M.Sidenav.init(sidenav);
	// form select initialization
	let select = document.querySelectorAll("select");
	M.FormSelect.init(select);
	// modal initialization
	let modals = document.querySelectorAll(".modal");
	M.Modal.init(modals);


	document.getElementById("formSubmit").addEventListener("click", function (event) {
		// Function to add error messages to form validation without redirecting the form. 
		event.preventDefault(); // Prevent the default form submission

		// Validate form fields
		let subject = document.getElementById("subject").value;
		let educationLevel = document.getElementById("education_level").value;
		let file = document.getElementById("file").value;

		if (!subject || !educationLevel) {
			// Display an error message on the page
			document.getElementById("errorMessage").innerText = "Please select both a subject and an education level.";
			return;
		}

		if (!file) {
			document.getElementById("errorMessage").innerText = "Please upload a file.";
			return;
		}

		// If validation passes, proceed with form submission
		document.getElementById("resourceForm").submit();
	});
});


// document.getElementById("my-link").addEventListener("click", function (e) {
// 	console.log("Click happened for: " + e.target.id);
// });


