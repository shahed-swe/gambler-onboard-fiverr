function pluralized(num) {
	if (num !== 1) {
		return 's';
	} else {
		return '';
	}
}

function trim(text, maxLength) {
	if (text.length > maxLength) {
		return text.substring(0, maxLength).trim() + '...';
	} else {
		return text.trim();
	}
}

function isUpperCase(string) {
	return string === string.toUpperCase();
}

export { pluralized, trim, isUpperCase };
