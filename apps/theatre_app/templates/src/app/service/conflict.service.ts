import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class ConflictService {
  constructor(private _http: Http) {}

  createConflict(conflict) {
    return this._http
      .post("/conflict", conflict)
      .map(data => data.json())
      .toPromise();
  }
  getConflict(conflict) {
    return this._http
      .get("/conflict", conflict)
      .map(data => data.json())
      .toPromise();
  }
  updateConflict(conflict) {
    return this._http
      .patch(`/conflcit/${conflict._id}`, conflict)
      .map(data => data.json())
      .toPromise();
  }

  destroyConflict(id: string) {
    return this._http
      .delete(`/conflict/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
