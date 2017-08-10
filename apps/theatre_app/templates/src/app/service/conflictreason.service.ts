import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class ConflictreasonService {
  constructor(private _http: Http) {}

  createConflictreason(conflictreason) {
    return this._http
      .post("/conflictreason", conflictreason)
      .map(data => data.json())
      .toPromise();
  }
  getConflictreason(conflictreason) {
    return this._http
      .get("/conflictreason")
      .map(data => data.json())
      .toPromise();
  }
  updateConflictreason(conflictreason) {
    return this._http
      .patch(`/conflcitreason/${conflictreason._id}`, conflictreason)
      .map(data => data.json())
      .toPromise();
  }

  destroyConflictreason(id: string) {
    return this._http
      .delete(`/conflictreason/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
