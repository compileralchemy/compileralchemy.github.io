title: Cell-based architecture
---
A cell-based architecture is real candy for enterprises. I sense it is a great Kubernetes companion. A cell-based architecture is traditionally introduced like compartments in a ship, containing water or fire spread. The cell contains damage, preventing disruption of the entire system. Services are designed to be autonomous and message-driven.

A cell consists of components. These can be monoliths or microservices or whatever. A cell is independently deployable, manageable, and observable. This is great if you ask me. Each cell has a control plane and a data plane. They can communicate outside with each other using a sidecar via a cell gateway. Communication planes inside a cell are called the local mesh and the communication planes outside the cells are called the global mesh. 

The components are grouped by key elements or functions which can also mirror an enterprise's team structure.

A cell can be scaled as needed.

Databases can occupy a cell or each cell can have its own database.

With pool architecture, each cell can have its client. This seems like a dreamland concept for Saas founders. Each client starts with a basic cell which can be scaled appropriately, with a consequent initial cost though.

Architecture reference: https://lnkd.in/dvPwQvVH
