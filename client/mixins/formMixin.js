export default {
	data() {
		return {
			submitted: false,
			submitting: false,
			success: false,
			error: null,
			errorFields: [],
			touchedFields: [],
			fieldDefaults: {},
		}
	},
	created() {
		if (this.$data.hasOwnProperty('fields')) {
			for (const [key, value] of Object.entries(this.$data.fields)) {
				this.$data.fieldDefaults[key] = value;
			}
		}
	},
	computed: {
		hasChanges() {
			return this.touchedFields.length > 0;
		},
	},
	methods: {
		handleError(error, errorFields, scrollTo) {
			this.submitting = false;
			this.error = error || 'You need to fix the errors below.';
			this.errorFields = errorFields;

			if (scrollTo !== null && scrollTo !== undefined) {
				window.scrollTo(0, scrollTo.offsetTop);
			}
		},
		beforeSubmit(fields, topElement) {
			this.submitted = true;
			this.success = false;
			this.error = null;

			if (!this.hasChanges) {
				this.error = 'You haven\'t made any changes!';
				return;
			}

			if (fields === undefined) {
				this.$v.$touch();
				if (this.$v.$invalid) {
					const invalidFields = this.getInvalidFields();
					this.handleError('The form is invalid', invalidFields, topElement);
				}
			} else {
				const invalidFields = this.areFieldsValid(fields);
				if (invalidFields.length > 0) {
					this.handleError('The form is invalid!', invalidFields, topElement);
				}
			}
		},
		getInvalidFields() {
			const invalid = [];
			Object.keys(this.$v.fields).forEach((field) => {
				if (this.$v.fields[field].$invalid) {
					invalid.push(field);
				}
			});
			return invalid;
		},
		areFieldsValid(fields) {
			const invalid = [];
			for (let i = 0; i < fields.length; i++) {
				const field = fields[i];
				this.$v.fields[field].$touch();
				if (this.$v.fields[field].$invalid) {
					invalid.push(field);
					if (!this.errorFields.includes(field)) {
						this.errorFields.push(field);
					}
				}
			}
			return invalid;
		},
		isFieldError(field) {
			return (this.submitted || this.touchedFields.includes(field)) && this.$v.fields[field] !== undefined && this.$v.fields[field].$invalid;
		},
		touchField(field) {
			this.error = null;
			this.success = false;

			if (!this.touchedFields.includes(field)) {
				this.touchedFields.push(field);
			}

			if (this.errorFields.includes(field)) {
				this.errorFields = this.errorFields.filter(existingField => field !== existingField);
			}
		},
		untouchFields(fields) {
			this.touchedFields = this.touchedFields.filter(field => !fields.includes(field));
			this.errorFields = this.errorFields.filter(field => !fields.includes(field));
		},
		resetForm() {
			for (const key of Object.keys(this.fields)) {
				if (this.fieldDefaults.hasOwnProperty(key)) {
					this.$data.fields[key] = this.fieldDefaults[key];
				} else {
					if (typeof key === 'number') {
						this.$data.fields[key] = 0;
					} else {
						this.$data.fields[key] = '';
					}
				}
			}

			this.submitted = false;
			this.submitting = false;
			this.error = null;
			this.errorFields = [];
			this.touchedFields = [];
		},
		createFileObject(file) {
			return {
				file,
				name: file.name,
				url: URL.createObjectURL(file),
				size: file.size
			}
		}
	}
}
