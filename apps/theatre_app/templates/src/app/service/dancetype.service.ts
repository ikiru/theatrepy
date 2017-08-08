import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class DancetypeService {
  constructor(private _http: Http) {}

  createDancetype(dancetype) {
    return this._http
      .post("/dancetype", dancetype)
      .map(data => data.json())
      .toPromise();
  }
  getDancetype(dancetype) {
    return this._http
      .get("/dancetype", dancetype)
      .map(data => data.json())
      .toPromise();
  }
  updateDancetype(dancetype) {
    return this._http
      .patch(`/dancetype/${dancetype._id}`, dancetype)
      .map(data => data.json())
      .toPromise();
  }

  destroyDancetype(id: string) {
    return this._http
      .delete(`/dancetype/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
