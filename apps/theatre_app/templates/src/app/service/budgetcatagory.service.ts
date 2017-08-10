import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class BudgetcatagoryService {
  constructor(private _http: Http) {}

  createBudgetcatagory(budgetcatagory) {
    return this._http
      .post("/budgetcatagory", budgetcatagory)
      .map(data => data.json())
      .toPromise();
  }
  getBudgetcatagory(budgetcatagory) {
    return this._http
      .get("/budgetcatagory")
      .map(data => data.json())
      .toPromise();
  }
  updateBudgetcatagory(budgetcatagory) {
    return this._http
      .patch(`/budgetcatagory/${budgetcatagory._id}`, budgetcatagory)
      .map(data => data.json())
      .toPromise();
  }

  destroyBudgetcatagory(id: string) {
    return this._http
      .delete(`/budgetcatagory/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
