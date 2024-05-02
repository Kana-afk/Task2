
Project Data Models
![image](https://github.com/Kana-afk/Task2/assets/73513054/3f03d7f4-a28e-44a1-9d14-b2ee796cf4d6)
![image](https://github.com/Kana-afk/Task2/assets/73513054/3a2d110c-448d-4484-964b-7908653ef1c0)
### Supplier

The `Supplier` model represents a supplier in the Supplier Relationship Management (SRM) system. It includes:
- **name**: The name of the supplier.
- **address**: The supplier's address.
- **phone**: Contact phone number.
- **email**: Email address.

This model stores essential information about the suppliers your company interacts with.

![image](https://github.com/Kana-afk/Task2/assets/73513054/51ca5e05-a250-4879-a7b9-900d09fc29b1)
### Contract

The `Contract` model manages agreements between the company and its suppliers. Key attributes include:
- **supplier**: A reference to the `Supplier` model.
- **contract_start**: Start date of the contract.
- **contract_end**: End date of the contract.
- **terms**: Text detailing the terms of the contract.

This model helps track the duration and conditions of supplier contracts.
![image](https://github.com/Kana-afk/Task2/assets/73513054/dad51e81-3dac-4d69-a567-44239674cfb6)
### Order

The `Order` model records orders placed with suppliers. It features:
- **supplier**: Linked to the `Supplier` model.
- **order_date**: The date the order was placed.
- **delivery_date**: Expected delivery date.
- **total_cost**: Total cost of the order.

This model is used to manage order details and logistics.
