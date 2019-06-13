
blogs={
	1:{
	"heading":"UDP stand for User Datagram Protocol .","img":"project1.jpg",
	"content":'''
		UDP stand for User Datagram Protocol .

Now let's see the code and then understand it.



import socket
t_host=input("Enter Host: ")
t_port=int(input("Enter Port: "))
#create socket object
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sending some data to client
client.sendto("AAABBBCCC",(t_host,t_port))
#now receive some data
data,ad=client.recvfrom(4096)
print(data)


We start by importing the socket module from standard library. Then we take input the Hostname and port from the user. After having the hostname and the port we create an object of socket class using

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
In this we have passed two parameters into the socket method, they are AF_INET and SOCK_DGRAM. Now the first parameter AF_INET states that we will be using standard IPV4 connection while SOCK_DGRAM states that we will be using UDP protocol .

After setting up we send the data using the sendto method which takes two parameters. The first parameter of sendto method is some data string and second is the tuple containing HOSTNAME and PORT.

Now to receive the response we use

data,ad=client.recvfrom(4096)
In this we can see that we get two values back and they are DATA and the ADDRESS from server. The recvfrom function is user to get response which takes an integer value of size of buffer to store response as parameter.



Note-We have made many assumptions here.These assumptions have been made to simplify our work. We can use Exception handling of sockets to avoid these.
	'''
	},
	2:{
	"heading":"React Native State and Props","img":"blog2.png",
	"content":"""React Native is a framework to develop ANDROID and IOS APP . It is based on Reactjs developed by facebook and is an open-source project. One of the most important concept of react native are states and props.

Let's dive into the code and then understand how it works.



const Name = props=>{
<Text>{props.name.name}</Text>
}
export default class NameApp extends Component{
constructor(){
super()
this.state={
names:[],
nameval:"",
}
}

addName(nameval){
this.setState({
name:[...this.state.names,{name:nameval}]
})
}
render(){
<View>
<Button title="ADD NAME" onPress={this.addName("Manish")} />
{this.state.names.map(name=(
<Name name={name} />
))}
</View>
}
}




Now lets Understand, now in constructor we see this.state, this is used to set the state variables and their default values. After setting the state variables we might need at some moment to change the value of that state for example here we have to add name on pressing on addname button. To change the value of state variables we call setState method and pass the new value of the variable. Here name:[...this.state.names,{name:nameval}] is used to set new value of names where ...this.state.names is so that it includes previous values as well. One more thing to understand is that the UI thread is updated each time we call setState method.



Saying about props , according to me they are just the parameters that are passed and accessed just like functions. In render function where we have written

<Name name={name} />

We have passed name as parameter which is then used in line

<Text> {props.name.name}</Text>

To get the name from props. props is only a simple variable that stores all other parameters passed on itself. """
	}
}