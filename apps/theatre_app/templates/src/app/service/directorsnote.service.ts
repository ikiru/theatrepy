import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class DirectorsnoteService {
  constructor(private _http: Http) {}

  createDirectorsnote(Directorsnote) {
    return this._http
      .post("/directorsnote", Directorsnote)
      .map(data => data.json())
      .toPromise();
  }
  getDirectorsnote(directorsnote) {
    return this._http
      .get("/directorsnote", directorsnote)
      .map(data => data.json())
      .toPromise();
  }
  updateDirectorsnote(directorsnote) {
    return this._http
      .patch(`/directorsnote/${directorsnote._id}`, directorsnote)
      .map(data => data.json())
      .toPromise();
  }

  destroyDirectorsnote(id: string) {
    return this._http
      .delete(`/directorsnote/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
