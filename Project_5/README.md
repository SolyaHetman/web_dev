# Course “Web Development and Web Design”
+ ## Project 5

### Author: *Solomia Hetman*


### [Here you can find our project](https://github.com/SolyaHetman/medical-service/tree/master/client/src/components/Doctor)


Axios is a very popular JavaScript library you can use to perform HTTP requests, that works in both Browser and Node.js platforms.

It supports all modern browsers, including support for IE8 and higher.

It is promise-based, and this lets us write async/await code to perform XHR requests very easily.

Using Axios has quite a few advantages over the native Fetch API:
<ul>
<li>supports older browsers (Fetch needs a polyfill)</li>
<li>has a way to abort a request</li>
<li>has a way to set a response timeout</li>
<li>has built-in CSRF protection</li>
<li>supports upload progress</li>
<li>performs automatic JSON data transformation</li>
Example

    var self = this;
        const id = this.$route.params.user;
        axios.get('http://localhost:3000/users',{
            params: {
            id: this.$route.params.user
            }
        })
        .then(function(res){
            self.users = res.data;
            console.log('Data :', res.data);
        })
        .catch(function(error){
            console.log('Error :', error)
        })
        }
```        