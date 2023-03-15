from typing import NamedTuple


class ValorantData(NamedTuple):
    knifes: list = ["58442f45-4783-42a2-f4cb-789a27555889", "9fb366b6-46df-a722-0cf2-9c9b85936f17",
                    "03de6b1a-4497-72e8-ae0c-2984b2e7e2b9",
                    "c5482640-4652-6948-29c6-769e8198db27", "9103fdf7-4361-5ac5-37ae-7cb51f13f45d",
                    "d034911c-45a6-1ce4-e6f5-4cbe57e9d4f1", "a486efac-4415-1bfa-68d1-19bca9968101",
                    "c3f1c9d6-441b-7def-1bf2-2c82719a4de8", "f91a1dd8-4f5f-bce4-f01d-4da95322c485",
                    "400bb847-4f4f-a39e-cd52-589f00b2204f", "8330a4c0-4e98-1cb7-9695-6b998b77138d",
                    "1ea64c8d-43c4-fce8-7354-01bdd6c0ee17", "6946cd0e-4e4a-ec4f-9238-dfb71715722b",
                    "ac687fc4-40c5-4c41-6a7c-5eb59adabd60", "31309f0b-49cd-295c-490d-96821a21c72f",
                    "71020826-483d-34f8-8da7-928f87942c10", "a4c41553-4ba5-efee-5685-7a9f0cdf7878",
                    "c91e4850-4d32-3b12-f411-3e9f644ea616", "ddc025b2-475f-889a-2800-80b4215582bc",
                    "f0c42e14-4a92-132d-dfd4-cbbef103340c", "1b8de6d7-4f37-7170-acd7-e78829f7959a",
                    "cd6ce089-43fa-c4dc-3f8f-0391cb604b5d", "6e0496c1-4c98-7abe-16c4-7ca3653e5cd8",
                    "94b40026-4efb-39ea-69d7-fca60be39c56", "151ee26c-4e82-e7ca-dad1-099e7fb34774",
                    "6417e12d-4f03-13d4-8704-20bf3a1bcb5b", "45129867-4977-e2a5-bead-cb828101b623",
                    "9a98f7dd-426c-603e-0569-e9b317c25ee4", "24cf2882-48c7-f287-155a-a4b6b083baa4",
                    "2640e9a6-415f-4c3e-cac0-16a24edb41c0", "ed792f00-43a7-cc88-b64b-b78c9de399a1",
                    "ccde2f25-4525-ef52-e1f0-bd88184bd4a4", "9c350ebe-458b-e6ed-ab77-2fb00cf249c1",
                    "c8b926df-4554-1b07-5a43-a9850bafca96", "dfe96f5a-4be0-c3f4-8e31-7f962bca2ade",
                    "e100dff1-4cf5-54ec-aa65-6fadbc22973b", "9237e734-4a2a-38ae-7438-6cbee901877d",
                    "908be835-43bc-b728-35a4-0fa91f612cc0", "6fa830c2-4924-87b2-1510-2fa4fbdca1db",
                    "0c07c7f3-4532-bc57-d474-26b3b39a38e6", "b1e9530d-4618-4f2e-1b75-f1a90c91b19e",
                    "f82aa022-4a6c-fa40-105d-92af6510ae1b", "83e8641b-41d0-821d-5eeb-5999e9294a0c",
                    "2e4300f9-49b3-6bbe-af7c-94a6f56ff12e", "46163791-47b9-2ef0-d255-aaa5146051bb",
                    "8e760310-4d95-354b-a910-049eaa4d2fc6", "16da5cca-49bc-2516-8ee6-c98d93e2d911",
                    "7d45aaad-4ac9-77b1-e7ca-3991be5721dd", "4af88517-4949-9caa-9dda-1980f07202a4",
                    "c18e781e-40a0-80e6-256a-54ae7355e7eb", "59f627f1-42f3-670d-5323-3499c2913289",
                    "f6cfd500-4eab-3c1d-9eeb-188e90731692", "ec04e1a4-4067-bb9c-c18b-46a80e5f3f1f",
                    "3209e2af-4703-088b-ebef-8da89b4cef87", "46664f5b-49ca-3e09-4fe5-56bdef536335",
                    "a590c03a-43b1-a408-4c6b-0bb9fdda1570", "206fc3fe-45a0-6c19-c367-229b98b6a2aa",
                    "4e7342a5-4820-2d79-a488-0fa51a4357f7", "feb4eb97-4ab3-793a-9a92-1b8af59dc023",
                    "c39f405f-42f1-acd1-a350-d3af39c32e33", "239ed20b-479c-e08e-c4b5-6ba0394576d4",
                    "07409307-46cc-98db-ec92-ceb04a865f73", "b5f42a00-425a-6fdf-61af-bb9a564c3d79",
                    "0357caf1-41a9-cb1c-c080-38aab13d9a7e", "6fd8cc46-48b3-f02c-46e3-cba372e7a328",
                    "52a1647c-42d9-b40e-16cf-a7821566ad81", "0aecb2b8-49cc-560e-42c7-6cbce44f05cf",
                    "b73d7b16-4652-bc5b-5c4c-068aabb19d0a", "f4e40444-43f3-e6f7-3271-bdb7d1492b05",
                    "2e77ac95-4681-3d87-bbdc-93a50ff6b1f6", "39cf499b-4f82-e875-5320-b0a1d7fc58d4",
                    "4f6033d5-4b24-94f0-31ab-f6969a2c926c", "5b95aba8-4223-e937-3ab7-9995c9e3064b",
                    "12cc9ed2-4430-d2fe-3064-f7a19b1ba7c7", "be489303-4aa4-ba46-e6a8-02ae4c7a7b3a",
                    "5724cd18-458b-af3d-b60a-239c5a8c081a", "5844ccd5-4a8d-e84d-b5b1-dfaaa8f34d84",
                    "c52fe5d7-4500-ffc0-cbcd-bfa29b7ea040", "e49c0fd2-435c-2c41-9164-4996080f455b"]
    regions: list = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV",
                     "LT",
                     "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "AL", "AD", "BY", "BA", "IS", "XK",
                     "MK",
                     "MD", "ME", "NO", "SM", "RS", "CH", "GB", "LA", "TR", "BR", "EU"]
    ranks: list = [
        "Iron 1", "Iron 2", "Iron 3",
        "Bronze 1", "Bronze 2", "Bronze 3",
        "Silver 1", "Silver 2", "Silver 3",
        "Gold 1", "Gold 2", "Gold 3",
        "Platinum 1", "Platinum 2", "Platinum 3",
        "Diamond 1", "Diamond 2", "Diamond 3",
        "Ascendant 1", "Ascendant 2", "Ascendant 3",
        "Immortal 1", "Immortal 2", "Immortal 3",
        "Radiant"
    ]


valorant_data = ValorantData()
