class FormData {
    constructor(context, types, urls) {
      this.context = context;
      this.types = types;
      this.urls = urls;
    }
  
    getContext() {
      return this.context;
    }
  
    setContext(context) {
      this.context = context;
    }
  
    getTypes() {
      return this.types;
    }
  
    setTypes(types) {
      this.types = types;
    }
  
    getUrls() {
      return this.urls;
    }
  
    setUrls(urls) {
      this.urls = urls;
    }
  
    addUrl(url) {
      this.urls.push(url);
    }
  
    removeUrl(url) {
      const index = this.urls.indexOf(url);
      if (index !== -1) {
        this.urls.splice(index, 1);
      }
    }
  }
  
  export default FormData;