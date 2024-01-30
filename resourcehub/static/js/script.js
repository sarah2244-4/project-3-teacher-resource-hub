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
});

document.getElementById("my-link").addEventListener("click", function (e) {
	console.log("Click happened for: " + e.target.id);
});
