const helloValidationSchema = {
  name: {
    isString: {
      errorMessage: 'error: not is string'
    },
    notEmpty: {
      errorMessage: 'error: is empty'
    }
  }
}

export default helloValidationSchema
