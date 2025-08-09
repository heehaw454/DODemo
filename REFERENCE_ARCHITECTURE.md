## Reference Architecture Diagram

Below is a simple reference architecture for the Flask SaaS app deployed on a DigitalOcean Kubernetes cluster:

```
+-----------------------------+
|    DigitalOcean LoadBalancer|
|         (Public IP/DNS)     |
+-------------+---------------+
              |
              v
+-----------------------------+
|      Kubernetes Service     |
|      (type: LoadBalancer)   |
+-------------+---------------+
              |
              v
+-----------------------------+
|      Kubernetes Pods        |
|   (Flask App Containers)    |
|  [Replicas: 3-5, Stateless] |
+-------------+---------------+
              |
              v
+-----------------------------+
|      Kubernetes Nodes       |
|   (DigitalOcean Droplets)   |
| [Default: 3, Autoscale: 5]  |
+-----------------------------+
```

**Key Points:**
- External users access the app via the DigitalOcean LoadBalancer (public IP/DNS).
- The LoadBalancer forwards traffic to the Kubernetes Service.
- The Service load balances requests to the Flask app pods.
- Pods are distributed across 3 (up to 5) DigitalOcean Droplet nodes.
- No persistent storage is attached; the app is stateless.

You can use tools like [draw.io](https://draw.io), [Lucidchart](https://lucidchart.com), or [Diagrams.net](https://diagrams.net) to create a visual version of this diagram for presentations