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
});
